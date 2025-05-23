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
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


    
def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

if __name__ == "__main__":
    patterns = ["apple", "app", "apricot", "banana"]
    trie = build_trie(patterns)
    
    print(trie.search("apple"))    
    print(trie.search("appl"))     
    print(trie.starts_with("app")) 
    print(trie.starts_with("ban")) 
    print(trie.starts_with("cat")) 
