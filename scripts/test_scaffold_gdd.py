"""Check the scaffold's file preservation, selection and generated data contracts."""

import csv
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("scaffold_gdd.py")
DOCUMENTS = {
    "00-one-pager.md", "01-vision.md", "02-core-loops.md", "03-world.md",
    "04-progression.md", "05-combat.md", "06-economy.md", "07-social-mmo.md",
    "08-endgame-liveops.md", "09-monetization.md", "10-art-audio.md",
    "11-tech-assumptions.md", "12-scope-roadmap.md", "13-risks.md",
    "GLOSSARY.md", "pitch/pitch-deck-outline.md", "pitch/buyer-brief.md",
}
# These are the public schemas in references/economy.md, independent of the
# implementation's CSV_HEADERS so an accidental schema change fails a test.
CSV_HEADERS = {
    "xp-curve.csv": ["level", "xp_required", "xp_cumulative", "est_hours", "est_hours_cumulative"],
    "items.csv": ["id", "name", "tier", "slot", "power", "value_g", "bind", "source"],
    "drop-tables.csv": ["mob_id", "item_id", "drop_rate", "min_qty", "max_qty", "pity_after"],
    "mob-stats.csv": ["id", "name", "level", "hp", "dps", "xp_reward", "gold_reward", "ttk_seconds"],
    "skills.csv": ["id", "name", "class", "cooldown", "cost", "damage_coeff", "unlock_level"],
    "economy-flow.csv": ["source_type", "name", "gold_per_hour", "player_level_band"],
}
ALL_FILES = DOCUMENTS | {"data/" + name for name in CSV_HEADERS}


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        self.root = Path(temp_dir.name) / "design folder"

    def scaffold(self, *options):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root), "--title", "Test", *options],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def files(self):
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*") if path.is_file()
        }

    def test_rerun_preserves_every_existing_file(self):
        self.scaffold()
        self.assertEqual(set(self.files()), ALL_FILES)
        for name in ALL_FILES:
            (self.root / name).write_bytes(("User content: " + name + "\n").encode("utf-8"))
        before = self.files()

        self.scaffold()

        self.assertEqual(self.files(), before)

    def test_partial_project_preserves_files_and_creates_missing_ones(self):
        existing = {
            "01-vision.md": b"Keep my vision\n",
            "GLOSSARY.md": b"Keep my names\n",
            "pitch/buyer-brief.md": b"Keep my pitch\n",
            "data/items.csv": b"id,name\n1,Custom Item\n",
        }
        for name, content in existing.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

        self.scaffold()

        after = self.files()
        self.assertEqual(set(after), ALL_FILES)
        for name, content in existing.items():
            with self.subTest(path=name):
                self.assertEqual(after[name], content)

    def test_only_accepts_padded_and_unpadded_numbers(self):
        for selection, expected in [
            ("1", {"01-vision.md"}),
            ("01", {"01-vision.md"}),
            ("0", {"00-one-pager.md"}),
            ("00", {"00-one-pager.md"}),
            ("12", {"12-scope-roadmap.md"}),
            (" 1,01, 06,6,12 ", {"01-vision.md", "06-economy.md", "12-scope-roadmap.md"}),
        ]:
            with self.subTest(selection=selection), tempfile.TemporaryDirectory() as temp_dir:
                self.root = Path(temp_dir) / "design"
                self.scaffold("--only", selection)
                # No unselected documents, pitch, glossary or CSV files.
                self.assertEqual(set(self.files()), expected)

    def test_only_preserves_an_existing_selected_file(self):
        self.root.mkdir(parents=True)
        (self.root / "01-vision.md").write_bytes(b"Keep this vision\n")
        self.scaffold("--only", "1,2")
        self.assertEqual(set(self.files()), {"01-vision.md", "02-core-loops.md"})
        self.assertEqual((self.root / "01-vision.md").read_bytes(), b"Keep this vision\n")

    def test_csv_files_have_documented_headers_and_no_data_rows(self):
        self.scaffold()
        self.assertEqual({path.name for path in (self.root / "data").iterdir()}, set(CSV_HEADERS))
        for name, header in CSV_HEADERS.items():
            with self.subTest(path=name):
                with (self.root / "data" / name).open(encoding="utf-8", newline="") as stream:
                    self.assertEqual(list(csv.reader(stream)), [header])

    def test_every_markdown_file_declares_its_open_question_count(self):
        self.scaffold()
        documents = {
            path.relative_to(self.root).as_posix(): path
            for path in self.root.rglob("*.md")
        }
        self.assertEqual(set(documents), DOCUMENTS)
        for name, path in documents.items():
            with self.subTest(path=name):
                content = path.read_text(encoding="utf-8")
                front_matter = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
                self.assertIsNotNone(front_matter, "Missing front matter in " + name)
                counts = re.findall(r"^open-questions: ([0-9]+)$", front_matter.group(1), re.MULTILINE)
                self.assertEqual(len(counts), 1, "Expected one open-questions field in " + name)
                self.assertEqual(int(counts[0]), content.count("[UNDECIDED"))


if __name__ == "__main__":
    unittest.main()
