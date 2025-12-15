class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        queue = deque()
        edge_regions = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1):
                    queue.append((r, c))
                    edge_regions.add((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O" and (nr, nc) not in edge_regions:
                    edge_regions.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in edge_regions:
                    board[r][c] = "X"
