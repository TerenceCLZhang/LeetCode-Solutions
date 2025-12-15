# Islands and Treasure on neetcode.io

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        distance = 1
        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        queue.append((nr, nc))

            distance += 1
