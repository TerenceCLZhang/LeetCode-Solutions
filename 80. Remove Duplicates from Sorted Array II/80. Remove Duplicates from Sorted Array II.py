from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return n

        left = 2
        for right in range(2, n):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        return left
