class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    queue = deque([(r, c)])
                    grid[r][c] = "0"
                    while queue:
                        cr, cc = queue.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
                    num_islands += 1

        return num_islands
