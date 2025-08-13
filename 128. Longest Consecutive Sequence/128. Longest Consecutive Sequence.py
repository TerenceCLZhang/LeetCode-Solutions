from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        largest = 0

        for n in unique:
            if n - 1 not in unique:
                current = 0
                while n in unique:
                    current += 1
                    n += 1
                largest = max(largest, current)

        return largest
