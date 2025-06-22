class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]

# Time: O(n + k log n)
# Space: O(1)
