class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        zero = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                left = zero + 1
                zero = right

            max_length = max(max_length, right - left)

        return max_length
