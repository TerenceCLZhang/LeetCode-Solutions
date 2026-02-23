class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            x, y = points[i]
            nx, ny = points[i + 1]
            time += max(abs(x - nx), abs(y - ny))
        return time