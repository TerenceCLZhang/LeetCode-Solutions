from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        minutes = 0
        num_fresh = 0

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    num_fresh += 1

        while queue:
            current_length = len(queue)
            minutes += 1
            for _ in range(current_length):
                i, j = queue.popleft()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        num_fresh -= 1
                        queue.append((ni, nj))

            if queue:
                minutes += 1

        return minutes if num_fresh == 0 else -1
