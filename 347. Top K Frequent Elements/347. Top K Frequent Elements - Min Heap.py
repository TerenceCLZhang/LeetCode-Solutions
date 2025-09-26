import heapq
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []

        for num, count in c.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappushpop(heap, (count, num))

        return [h[1] for h in heap]
