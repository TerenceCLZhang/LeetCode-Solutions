class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if r == l:
                return i
            l += nums[i]
        return -1

# Time: O(n)
# Space: O(1)