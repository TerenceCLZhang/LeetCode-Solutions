class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = deque()
        l = 0
        r = len(nums) - 1

        while l <= r:
            low_squared = nums[l] ** 2
            high_squared = nums[r] ** 2
            if low_squared > high_squared:
                ans.appendleft(low_squared)
                l += 1
            else:
                ans.appendleft(high_squared)
                r -= 1

        return list(ans)

# Time: O(n)
# Space: O(n)