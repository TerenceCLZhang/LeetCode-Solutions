from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)

        for j in range(9):
            seen = set()
            for i in range(9):
                cell = board[i][j]
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)

        grid_starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                       (3, 6), (6, 0), (6, 3), (6, 6)]

        for start_x, start_y in grid_starts:
            seen = set()
            for i in range(start_x, start_x + 3):
                for j in range(start_y, start_y + 3):
                    cell = board[i][j]
                    if cell != ".":
                        if cell in seen:
                            return False
                        seen.add(cell)

        return True
