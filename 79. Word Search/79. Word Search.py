from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)

        def backtrack(i, j, index):
            if index == w:
                return True

            if i < 0 or i >= m or j < 0 or j >= n or word[index] != board[i][j]:
                return False

            char = board[i][j]
            board[i][j] = "#"

            found = backtrack(i + 1, j, index + 1) or backtrack(i - 1, j, index +
                                                                1) or backtrack(i, j + 1, index + 1) or backtrack(i, j - 1, index + 1)

            board[i][j] = char
            return found

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False
