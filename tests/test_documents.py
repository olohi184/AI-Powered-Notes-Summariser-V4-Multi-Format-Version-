"""Fast unit tests that do not download an AI model."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from notes_summariser.documents import extract_text
from notes_summariser.summarize import chunk_text


class NotesTests(unittest.TestCase):
    def test_text_document(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "notes.txt"
            file.write_text("  Research notes.  ", encoding="utf-8")
            self.assertEqual(extract_text(file), "Research notes.")

    def test_unsupported_extension(self):
        with self.assertRaises(ValueError):
            extract_text("notes.csv")

    def test_chunking_preserves_words(self):
        text = "one two three four five"
        self.assertEqual(chunk_text(text, max_words=2), ["one two", "three four", "five"])

    def test_empty_document(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "empty.txt"
            file.write_text("  ", encoding="utf-8")
            with self.assertRaises(ValueError):
                extract_text(file)


if __name__ == "__main__":
    unittest.main()
