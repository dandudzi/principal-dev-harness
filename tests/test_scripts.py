import unittest
from pathlib import Path


class ScriptTests(unittest.TestCase):
    def test_scripts_compile(self):
        scripts_dir = Path(__file__).resolve().parents[1] / "scripts"
        self.assertTrue(scripts_dir.is_dir(), "The scripts directory is missing")

        for script in sorted(scripts_dir.rglob("*.py")):
            with self.subTest(script=script.relative_to(scripts_dir)):
                compile(script.read_bytes(), str(script), "exec")
