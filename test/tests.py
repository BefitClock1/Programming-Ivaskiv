import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab9_main import find_longest_chain, read_words

class TestGraph(unittest.TestCase):
    def test_flow(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'wchain.txt')
        file_path = os.path.abspath(file_path)  

        words = read_words(file_path)
        result, chain = find_longest_chain(words)
        self.assertEqual(result,6)  


if __name__ == "__main__":
    unittest.main()
