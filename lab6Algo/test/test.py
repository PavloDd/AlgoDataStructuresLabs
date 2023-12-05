import unittest
from src.main import Trie


class TrieTest(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.trie.insert("banana")

        self.assertEqual(self.trie.search("apple"), True)
        self.assertEqual(self.trie.search("app"), True)
        self.assertEqual(self.trie.search("apricot"), True)
        self.assertEqual(self.trie.search("banana"), True)
        self.assertEqual(self.trie.search("grape"), False)

    def test_starts_with_prefix(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.trie.insert("banana")

        self.assertEqual(self.trie.starts_with_prefix("ap"), True)
        self.assertEqual(self.trie.starts_with_prefix("ban"), True)
        self.assertEqual(self.trie.starts_with_prefix("gr"), False)


if __name__ == '__main__':
    unittest.main()

