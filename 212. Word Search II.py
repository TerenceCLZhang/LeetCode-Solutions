class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end_of_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for w in words:
            trie.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        ans, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word.append(board[r][c])

            if node.end_of_word:
                ans.add("".join(word))
                # pruning - remove word from trie after it has been added to ans
                node.end_of_word = False

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, node, word)

            word.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, [])

        return list(ans)
