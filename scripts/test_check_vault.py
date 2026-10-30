"""Regression tests for the vault checker's two supported checks."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.check_vault import check_vault


SCRIPTS = Path(__file__).resolve().parent


class VaultTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "check_vault.py"), *map(str, arguments)],
            capture_output=True, text=True,
        )

    def test_scaffold_is_clean(self):
        subprocess.run(
            [sys.executable, str(SCRIPTS / "scaffold_gdd.py"), str(self.root), "--title", "Test"],
            check=True, capture_output=True,
        )
        self.assertEqual(len(list(self.root.rglob("*.md"))), 17)
        self.assertEqual(check_vault(self.root), [])
        self.assertEqual(self.cli(self.root).returncode, 0)

    def test_valid_links_paths_aliases_headings_and_attachments(self):
        self.write("systems/Economy.md", "# Economy\n## Gold flow ###\n## `Silver`\n\nItem table\n----------\n")
        self.write("data/items.csv", "id,name\n")
        self.write("notes/index.md", "\n".join([
            "# Local", "[[systems/Economy#Gold flow|gold]]",
            r"| [[systems/Economy.md#Gold flow\|gold]] |",
            "[[../systems/Economy#Silver]]", "[[Economy#Item table]]",
            "[[#Local]]", "[[data/items.csv]]", "![[systems/Economy]]",
        ]))
        self.assertEqual(check_vault(self.root), [])

    def test_reports_each_broken_link_at_its_source_line(self):
        self.write("target.md", "# Exists\n")
        self.write("nested/source.md", "# Source\n\n[[missing]] [[target#Gone|alias]]\n[[#Gone]]\n")
        self.assertEqual(check_vault(self.root), [
            ("nested/source.md", 3, "missing file 'missing'"),
            ("nested/source.md", 3, "missing heading 'Gone' in 'target.md'"),
            ("nested/source.md", 4, "missing heading 'Gone' in 'nested/source.md'"),
        ])

    def test_ignores_code_comments_front_matter_and_escaped_links(self):
        self.write("source.md", "\n".join([
            "---", 'example: "[[missing]]"', "---",
            "`[[missing]]` and ``a ` [[missing]]``",
            "`multiline", "[[missing]]`", r"\[[missing]]",
            "<!-- [[missing]]", "[[missing]] -->", "```markdown",
            "[[missing]]", "~~~", "[[missing]]", "```", "~~~~",
            "[[missing]]", "~~~", "[[missing]]", "~~~~", "",
            "    [[missing]]", "\t[[missing]]", "[[real-missing]]",
        ]))
        self.assertEqual(check_vault(self.root), [("source.md", 23, "missing file 'real-missing'")])

    def test_fake_headings_in_code_and_comments_do_not_resolve(self):
        self.write("target.md", "```\n# Fake\n```\n<!--\n# Hidden\n-->\n")
        self.write("source.md", "[[target#Fake]]\n[[target#Hidden]]\n")
        self.assertEqual(len(check_vault(self.root)), 2)
        self.assertTrue(all("missing heading" in item[2] for item in check_vault(self.root)))

    def test_literal_syntax_does_not_hide_later_links(self):
        cases = [
            ("<!--\n```\n-->\n[[missing]]\n", 4),
            ("`<!--`\n[[missing]]\n", 2),
            ("```\n<!--\n```\n[[missing]]\n", 4),
            ("````\n```\n[[example]]\n````\n[[missing]]\n", 5),
        ]
        for content, line in cases:
            with self.subTest(content=content):
                self.write("source.md", content)
                self.assertEqual(check_vault(self.root), [("source.md", line, "missing file 'missing'")])

    def test_formatted_headings_preserve_meaningful_underscores(self):
        self.write("target.md", "# **Gold**\n## *Silver*\n## __Copper__\n## class_id\n")
        self.write("source.md", "[[target#Gold]] [[target#Silver]] [[target#Copper]] [[target#class_id]]\n")
        self.assertEqual(check_vault(self.root), [])

    def test_extended_references_are_not_misreported_as_missing_headings(self):
        self.write("target.md", "# Parent\n## Child\nParagraph ^block\n")
        self.write("source.md", "[[target#Parent#Child]]\n[[target#^block]]\n")
        problems = check_vault(self.root)
        self.assertEqual(len(problems), 2)
        self.assertTrue(all("unsupported heading reference" in item[2] for item in problems))

    def test_utf8_bom_and_crlf_preserve_line_numbers(self):
        (self.root / "source.md").write_bytes(b"\xef\xbb\xbf---\r\nopen-questions: 0\r\n---\r\n[[missing]]\r\n")
        self.assertEqual(check_vault(self.root), [("source.md", 4, "missing file 'missing'")])

    def test_bare_name_prefers_sibling_and_ambiguous_names_are_reported(self):
        self.write("a/note.md", "# A\n")
        self.write("b/note.md", "# B\n")
        self.write("a/index.md", "[[note#A]]\n")
        self.write("index.md", "[[note]]\n")
        self.assertEqual(check_vault(self.root), [("index.md", 1, "ambiguous file 'note'; use a folder path")])

    def test_markers_count_every_literal_occurrence(self):
        self.write("source.md", "---\nopen-questions: 3 # pending\n---\n[UNDECIDED: A] [UNDECIDED: B]\n`[UNDECIDED: C]`\n")
        self.assertEqual(check_vault(self.root), [])

    def test_mismatch_is_reported_on_front_matter_field_line(self):
        self.write("source.md", "---\ntitle: Test\nopen-questions: 2\n---\n[UNDECIDED: A]\n")
        self.assertEqual(check_vault(self.root), [("source.md", 3, "open-questions is 2 but found 1 [UNDECIDED markers")])

    def test_zero_markers_with_or_without_metadata(self):
        self.write("GLOSSARY.md", "# Glossary\n")
        self.write("complete.md", "---\nopen-questions: 0\n---\n# Done\n")
        self.assertEqual(check_vault(self.root), [])

    def test_missing_count_with_markers_is_reported(self):
        self.write("source.md", "[UNDECIDED: A]\n")
        self.assertEqual(check_vault(self.root), [("source.md", 1, "missing open-questions field for 1 markers")])

    def test_body_field_is_not_front_matter(self):
        self.write("source.md", "# Note\nopen-questions: 99\n")
        self.assertEqual(check_vault(self.root), [])

    def test_bad_counts_and_duplicate_fields(self):
        for value in ("-1", "1.5", "unknown", "", '"0"'):
            with self.subTest(value=value):
                self.write("source.md", "---\nopen-questions: %s\n---\n" % value)
                self.assertEqual(check_vault(self.root), [("source.md", 2, "open-questions must be a non-negative integer")])
        self.write("source.md", "---\nopen-questions: 0\nopen-questions: 0\n---\n")
        self.assertEqual(check_vault(self.root), [("source.md", 3, "duplicate open-questions field")])

    def test_unclosed_front_matter_is_reported(self):
        self.write("source.md", "---\nopen-questions: 0\n")
        self.assertEqual(check_vault(self.root), [("source.md", 1, "unclosed front matter")])

    def test_invalid_utf8_is_a_finding(self):
        (self.root / "bad.md").write_bytes(b"\xff")
        problems = check_vault(self.root)
        self.assertEqual(problems[0][:2], ("bad.md", 1))
        self.assertIn("cannot read Markdown", problems[0][2])

    def test_link_cannot_escape_vault(self):
        self.write("source.md", "[[../outside]]\n")
        self.assertEqual(check_vault(self.root), [("source.md", 1, "link points outside the vault")])

    def test_cli_reports_all_findings_without_changing_files(self):
        self.write("source.md", "---\nopen-questions: 1\n---\n[[missing]]\n")
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.root.rglob("*") if p.is_file()}
        result = self.cli(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("source.md:2: open-questions is 1 but found 0", result.stdout)
        self.assertIn("source.md:4: missing file 'missing'", result.stdout)
        self.assertEqual(result.stderr, "")
        self.assertEqual({p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.root.rglob("*") if p.is_file()}, before)

    def test_invalid_input_directory_exits_two(self):
        for path in (self.root / "missing", self.write("file.md", "# File\n")):
            with self.subTest(path=path):
                result = self.cli(path)
                self.assertEqual(result.returncode, 2)
                self.assertIn("existing directory", result.stderr)


if __name__ == "__main__":
    unittest.main()
