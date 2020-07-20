import unittest
from pybootstrap import file_content


class TestFileContent(unittest.TestCase):
    def test_1(self):
        self.assertIsInstance(file_content.setup("xx", "xx"), str)


if __name__ == "__main__":
    unittest.main()
