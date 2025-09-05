class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.data = []  # store player/team info
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, data=None):
        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        if data:
            node.data.append(data)

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.extend(node.data)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix: str):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix, results)
        return results
