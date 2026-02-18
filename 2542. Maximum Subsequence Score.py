class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted([(n1, n2) for n1, n2 in zip(nums1, nums2)],
                       key=lambda p: p[1], reverse=True)
        heap = []

        n1_sum = 0
        res = 0

        for n1, n2 in pairs:
            n1_sum += n1
            heapq.heappush(heap, n1)

            if len(heap) > k:
                n1_pop = heapq.heappop(heap)
                n1_sum -= n1_pop

            if len(heap) == k:
                res = max(res, n1_sum * n2)

        return res
