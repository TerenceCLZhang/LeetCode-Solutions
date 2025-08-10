from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in complement:
                return [complement[needed], i]
            complement[n] = i
