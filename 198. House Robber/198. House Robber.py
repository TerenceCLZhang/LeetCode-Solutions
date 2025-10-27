from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        rob1 = nums[0]
        rob2 = max(rob1, nums[1])

        for i in range(2, n):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])

        return rob2
