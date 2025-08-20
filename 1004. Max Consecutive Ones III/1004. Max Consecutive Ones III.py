from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_flipped = 0
        left = 0
        max_length = 0

        for curr in range(len(nums)):
            if nums[curr] == 0:
                num_flipped += 1

            while num_flipped > k:
                if nums[left] == 0:
                    num_flipped -= 1

                left += 1

            curr_length = curr - left + 1
            max_length = max(max_length, curr_length)

        return max_length
