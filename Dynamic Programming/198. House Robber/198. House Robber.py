class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[i - 1])
            else:
                nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        
        return nums[-1]

# Time: O(n)
# Space: O(1)