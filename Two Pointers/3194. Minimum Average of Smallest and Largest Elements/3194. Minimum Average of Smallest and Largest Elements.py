class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = float("inf")
        l = 0
        r = len(nums) - 1

        while l < r:
            min_avg = min(min_avg, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        
        return min_avg

# Time: O(n log n)
# Space: O(1)