class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        summ = 0
        min_length = float("inf")

        for i in range(len(nums)):
            summ += nums[i]
            
            while summ >= target:
                min_length = min(min_length, i - start + 1)
                summ -= nums[start]
                start += 1
        
        return min_length if min_length != float("inf") else 0

# Time: O(n)
# Space: O(1)