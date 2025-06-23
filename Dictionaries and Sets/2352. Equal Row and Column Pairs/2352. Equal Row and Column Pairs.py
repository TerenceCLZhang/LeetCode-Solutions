class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1

        pairs = 0
        for j in range(len(grid)):
            key = []
            for i in range(len(grid)):
                key.append(grid[i][j])
            key = tuple(key)
            if key in rows:
                pairs += rows[key]

        return pairs

# Time: O(n^2)
# Space: O(n)