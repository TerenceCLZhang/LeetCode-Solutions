class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        minn = min(nums)
        maxx = max(nums)

        for n in nums:
            if n != minn and n != maxx:
                return n

# Time: O(n)
# Space: O(1)