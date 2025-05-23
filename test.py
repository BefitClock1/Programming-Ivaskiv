import unittest
from lab_7_src import Trie, build_trie  

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.words = ["apple", "app", "apricot", "banana"]
        for word in self.words:
            self.trie.insert(word)

    def test_search_existing_words(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apricot"))
        self.assertTrue(self.trie.search("banana"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("appl"))   
        self.assertFalse(self.trie.search("bananas"))
        self.assertFalse(self.trie.search(""))

    def test_starts_with_true(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apr"))
        self.assertTrue(self.trie.starts_with("ban"))

    def test_starts_with_false(self):
        self.assertFalse(self.trie.starts_with("cat"))
        self.assertFalse(self.trie.starts_with("z"))

if __name__ == '__main__':
    unittest.main()
