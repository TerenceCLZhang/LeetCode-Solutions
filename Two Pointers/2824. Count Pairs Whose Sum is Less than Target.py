class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        pairs = 0

        while lo < hi:
            if nums[lo] + nums[hi] < target:
                pairs += hi - lo
                lo += 1
            else:
                hi -= 1

        return pairs

# Time: O(n log n)
# Space: O(1)