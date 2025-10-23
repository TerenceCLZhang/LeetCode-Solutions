from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        # Left and right edges
        for i in range(m):
            p_queue.append((i, 0))
            p_seen.add((i, 0))

            a_queue.append((i, n - 1))
            a_seen.add((i, n - 1))

        # Top and bottom edges
        for j in range(n):
            p_queue.append((0, j))
            p_seen.add((0, j))

            a_queue.append((m - 1, j))
            a_seen.add((m - 1, j))

        def bfs(q, seen):
            while q:
                x, y = q.popleft()

                for dx, dy, in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and heights[x][y] <= heights[nx][ny]:
                        seen.add((nx, ny))
                        q.append((nx, ny))

        bfs(p_queue, p_seen)
        bfs(a_queue, a_seen)
        return list(p_seen.intersection(a_seen))
