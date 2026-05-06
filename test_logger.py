import unittest
import os
import tempfile
from logger import Logger

class TestLogger(unittest.TestCase):

    def test_log_writes_to_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp_path = temp.name

        logger = Logger(filename=temp_path)
        logger.log("Test entry")

        with open(temp_path, "r") as f:
            content = f.read()

        os.remove(temp_path)
        self.assertIn("Test entry", content)

if __name__ == "__main__":
    unittest.main()

