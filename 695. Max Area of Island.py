class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue = deque([(r, c)])
                    area = 0
                    while queue:
                        area += 1
                        cr, cc = queue.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                    max_area = max(max_area, area)

        return max_area
