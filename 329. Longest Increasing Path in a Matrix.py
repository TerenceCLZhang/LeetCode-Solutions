class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[1] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if dp[r][c] != 1:
                return dp[r][c]

            longest = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] < matrix[r][c]:
                    longest = max(longest, dfs(nr, nc))

            dp[r][c] += longest
            return dp[r][c]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)

        return max(path for row in dp for path in row)
