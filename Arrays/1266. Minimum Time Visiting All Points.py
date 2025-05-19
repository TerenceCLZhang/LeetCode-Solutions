class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            current = points[i]
            nextt = points[i + 1]
            x = abs(nextt[0] - current[0])
            y = abs(nextt[1] - current[1])
            time += max(x, y)
        
        return time

# Time: O(n)
# Space: O(1)