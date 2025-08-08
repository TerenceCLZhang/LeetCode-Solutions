from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        summary_ranges = []
        start = 0

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    summary_ranges.append(f"{nums[start]}")
                else:
                    summary_ranges.append(f"{nums[start]}->{nums[i - 1]}")
                start = i

        return summary_ranges
