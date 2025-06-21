class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            sett = set()
            for j in range(9):
                if board[i][j] in sett:
                    return False
                elif board[i][j] != ".":
                    sett.add(board[i][j])

        for i in range(9):
            sett = set()
            for j in range(9):
                if board[j][i] in sett:
                    return False
                elif board[j][i] != ".":
                    sett.add(board[j][i])

        starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                  (3, 6), (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            sett = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] in sett:
                        return False
                    elif board[row][col] != ".":
                        sett.add(board[row][col])

        return True

# Time: O(1)
# Space: O(1)
