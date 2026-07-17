class Trie(object):

    def __init__(self):
        self.Trie = {}

    def insert(self, word):
        d = self.Trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["."] = word    

class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        seen = set()

        def dfs(i, j, node):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in seen:
                return
            c = board[i][j]
            if c not in node:
                return

            next_node = node[c]

            if "." in next_node:
                res.append(next_node["."])
                del next_node["."]
            seen.add((i, j))

            dfs(i + 1, j, next_node)
            dfs(i - 1, j, next_node)
            dfs(i, j + 1, next_node)
            dfs(i, j - 1, next_node)

            seen.remove((i, j))

            if not next_node:
                del node[c]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.Trie)

        return res
