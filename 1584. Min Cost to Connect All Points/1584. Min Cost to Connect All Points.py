from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = 0
        seen = set()
        min_heap = [(0, 0)]

        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)

            if i in seen:
                continue

            seen.add(i)
            cost += dist

            x, y = points[i]

            for j in range(len(points)):
                if j not in seen:
                    other_x, other_y = points[j]
                    man_dist = abs(x - other_x) + abs(y - other_y)
                    heapq.heappush(min_heap, (man_dist, j))

        return cost
