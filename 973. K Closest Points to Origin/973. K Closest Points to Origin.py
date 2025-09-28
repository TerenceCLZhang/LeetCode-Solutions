from typing import List
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            distance = -(p[0] ** 2 + p[1] ** 2)

            if len(heap) < k:
                heapq.heappush(heap, (distance, p))
            else:
                heapq.heappushpop(heap, (distance, p))

        return [h[1] for h in heap]
