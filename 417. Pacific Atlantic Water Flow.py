class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        p_queue, a_queue = deque(), deque()
        p_heights, a_heights = set(), set()

        for r in range(ROWS):
            p_queue.append((r, 0))
            p_heights.add((r, 0))

            a_queue.append((r, COLS - 1))
            a_heights.add((r, COLS - 1))

        for c in range(COLS):
            p_queue.append((0, c))
            p_heights.add((0, c))

            a_queue.append((ROWS - 1, c))
            a_heights.add((ROWS - 1, c))

        def bfs(queue, sett):
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] <= heights[nr][nc] and (nr, nc) not in sett:
                        sett.add((nr, nc))
                        queue.append((nr, nc))

        bfs(p_queue, p_heights)
        bfs(a_queue, a_heights)

        return list(p_heights & a_heights)
