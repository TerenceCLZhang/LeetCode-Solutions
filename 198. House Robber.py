class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2 = 0
        prev1 = 0

        for n in nums:
            not_rob = prev1
            rob = prev2 + n
            prev2, prev1 = prev1, max(not_rob, rob)

        return prev1
