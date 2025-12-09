class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        mins = 0
        num_fresh = 0
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        changed = True
        while num_fresh > 0 and changed:
            changed = False
            length = len(queue)
            for _ in range(length):
                cr, cc = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        num_fresh -= 1
                        changed = True

            mins += 1

        return mins if num_fresh == 0 else -1
