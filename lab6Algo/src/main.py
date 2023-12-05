class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie


patterns = ["apple", "app", "apricot", "banana"]
trie = build_trie(patterns)


print(trie.search("apple"))
print(trie.search("app"))
print(trie.search("apricot"))
print(trie.search("banana"))
print(trie.search("grape"))
print("-------------------")
print(trie.starts_with_prefix("ap"))
print(trie.starts_with_prefix("ban"))
print(trie.starts_with_prefix("gr"))
