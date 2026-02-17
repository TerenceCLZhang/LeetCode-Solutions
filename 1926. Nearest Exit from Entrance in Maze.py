class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        steps = 0
        queue = deque([entrance])
        visited = set([entrance[0], entrance[1]])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and [r, c] != entrance and maze[r][c] == ".":
                    return steps

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and maze[nr][nc] == ".":
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            steps += 1

        return -1
