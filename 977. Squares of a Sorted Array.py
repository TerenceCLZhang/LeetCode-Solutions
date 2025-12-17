class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1

        ans = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans.append(nums[left] ** 2)
                left += 1
            else:
                ans.append(nums[right] ** 2)
                right -= 1

        return ans[::-1]
