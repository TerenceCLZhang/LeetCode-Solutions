class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            low_squared = nums[l] ** 2
            high_squared = nums[r] ** 2
            if low_squared > high_squared:
                ans.append(low_squared)
                l += 1
            else:
                ans.append(high_squared)
                r -= 1

        ans.reverse()
        return ans

# Time: O(n)
# Space: O(n)