class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        pairs = 0
        rows = defaultdict(int)

        for r in range(n):
            rows[tuple(grid[r])] += 1

        for c in range(n):
            col = tuple([grid[r][c] for r in range(n)])
            pairs += rows[col]

        return pairs
