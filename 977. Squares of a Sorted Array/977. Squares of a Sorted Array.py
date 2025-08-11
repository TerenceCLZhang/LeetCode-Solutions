from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_sorted = []
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2

            if left_squared > right_squared:
                squared_sorted.append(left_squared)
                left += 1
            else:
                squared_sorted.append(right_squared)
                right -= 1

        squared_sorted.reverse()

        return squared_sorted
