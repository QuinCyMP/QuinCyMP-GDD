"""Exercise genre presets through the public CLI, using only the standard library."""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'scaffold_gdd.py'


class GenreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_cli(self, target, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(target), '--title', 'Test', *args],
            capture_output=True, text=True,
        )

    def snapshot(self, target):
        return {p.relative_to(target): p.read_bytes()
                for p in target.rglob('*') if p.is_file()}

    def test_default_matches_explicit_mmo(self):
        default, explicit = self.root / 'default', self.root / 'explicit'
        self.assertEqual(self.run_cli(default).returncode, 0)
        self.assertEqual(self.run_cli(explicit, '--genre', 'mmo').returncode, 0)
        self.assertEqual(self.snapshot(default), self.snapshot(explicit))
        self.assertEqual(len(self.snapshot(default)), 23)
        self.assertTrue((default / '07-social-mmo.md').exists())

    def test_roguelike_files_and_questions(self):
        self.assertEqual(self.run_cli(self.root, '--genre', 'roguelike').returncode, 0)
        self.assertEqual(len(self.snapshot(self.root)), 19)
        for name in ('07-social-mmo.md', '08-endgame-liveops.md',
                     'data/xp-curve.csv', 'data/economy-flow.csv'):
            self.assertFalse((self.root / name).exists(), name)
        progression = (self.root / '04-progression.md').read_text()
        self.assertIn('## Reset rules', progression)
        self.assertIn('## Between runs', progression)
        self.assertNotIn('A new player in year two', progression)
        self.assertNotIn('MMO', (self.root / '12-scope-roadmap.md').read_text())
        for path in self.root.rglob('*.md'):
            if path.name == 'GLOSSARY.md':
                continue  # The unchanged glossary has no question metadata.
            content = path.read_text()
            count = int(re.search(r'^open-questions: (\d+)$', content, re.M)[1])
            self.assertEqual(count, content.count('[UNDECIDED:'), path.name)

    def test_only_intersects_preset_and_omits_supporting_files(self):
        self.assertEqual(self.run_cli(self.root, '--genre', 'roguelike',
                                     '--only', '04,07').returncode, 0)
        self.assertEqual(set(self.snapshot(self.root)), {Path('04-progression.md')})
        empty = self.root / 'empty'
        self.assertEqual(self.run_cli(empty, '--genre', 'roguelike',
                                     '--only', '07').returncode, 0)
        self.assertFalse(empty.exists())

    def test_reruns_and_genre_changes_preserve_existing_files(self):
        self.assertEqual(self.run_cli(self.root, '--genre', 'roguelike').returncode, 0)
        for path in self.root.rglob('*'):
            if path.is_file():
                path.write_bytes(b'User content\n')
        before = self.snapshot(self.root)
        for genre in ('roguelike', 'mmo'):
            self.assertEqual(self.run_cli(self.root, '--genre', genre).returncode, 0)
            after = self.snapshot(self.root)
            for path, content in before.items():
                self.assertEqual(after[path], content, path)

    def test_invalid_genre_creates_nothing(self):
        result = self.run_cli(self.root, '--genre', 'unknown')
        self.assertEqual(result.returncode, 2)
        self.assertIn('invalid choice', result.stderr)
        self.assertEqual(self.snapshot(self.root), {})

    def test_help_lists_genres(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--help'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('--genre {mmo,roguelike}', result.stdout)
        self.assertIn('default: mmo', result.stdout)


if __name__ == '__main__':
    unittest.main()
