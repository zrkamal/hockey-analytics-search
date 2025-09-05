class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.data = []  # store player/team info

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, data=None):
        key = key.strip().lower()  # normalize key
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        if data:
            node.data.append(data)

    def _dfs(self, node, results):
        """DFS to collect all entries under a node"""
        if node.is_end_of_word:
            results.extend(node.data)
        for child in node.children.values():
            self._dfs(child, results)

    def autocomplete(self, prefix: str, log_nodes=False):
        prefix = prefix.strip().lower()  # normalize query
        node = self.root
        nodes_visited = 0

        for char in prefix:
            if char not in node.children:
                return ([], nodes_visited) if log_nodes else []
            node = node.children[char]
            nodes_visited += 1

        results = []
        self._dfs(node, results)

        if log_nodes:
            # Count all nodes under this prefix for logging
            total_nodes = self._count_nodes(node)
            nodes_visited += total_nodes - 1  # root node already counted
            return results, nodes_visited

        return results

    def _count_nodes(self, node):
        """Count all nodes under a node"""
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count
