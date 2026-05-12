import unittest
import os
import tempfile
from logger import Logger

class TestLogger(unittest.TestCase):
    """Tests for the Logger class"""

    def test_log_writes_to_file(self):
        """A logged entry should appear in the output file"""
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp_path = temp.name
        logger = Logger(filename=temp_path)
        logger.log("Test entry")
        with open(temp_path, "r") as f:
            content = f.read()
        os.remove(temp_path)
        self.assertIn("Test entry", content)

    def test_header_written_on_init(self):
        """Logger should write the 'Mindfulness Log' header when created"""
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp_path = temp.name
        Logger(filename=temp_path)
        with open(temp_path, "r") as f:
            content = f.read()
        os.remove(temp_path)
        self.assertIn("Mindfulness Log", content)

    def test_multiple_entries_all_present(self):
        """All logged entries should be present in the file"""
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp_path = temp.name
        logger = Logger(filename=temp_path)
        logger.log("First exercise")
        logger.log("Second exercise")
        with open(temp_path, "r") as f:
            content = f.read()
        os.remove(temp_path)
        self.assertIn("First exercise", content)
        self.assertIn("Second exercise", content)


if __name__ == "__main__":
    unittest.main()

