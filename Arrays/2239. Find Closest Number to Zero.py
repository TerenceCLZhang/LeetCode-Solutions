class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c = nums[0]
        for n in nums:
            if abs(n) < abs(c) or abs(c) == abs(n) and n > c:
                c = n
        return c

# Time: O(n)
# Space: O(1)