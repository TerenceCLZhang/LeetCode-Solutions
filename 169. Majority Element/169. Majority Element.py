from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_element = None
        count = 0

        for n in nums:
            if count <= 0:
                curr_element = n

            if n == curr_element:
                count += 1
            else:
                count -= 1

        return curr_element
