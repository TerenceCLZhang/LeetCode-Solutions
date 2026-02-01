class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        left = 0
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                min_size = min(min_size, right - left + 1)
                summ -= nums[left]
                left += 1

        return min_size if min_size != float("inf") else 0
