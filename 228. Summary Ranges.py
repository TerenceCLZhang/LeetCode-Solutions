class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        ranges = []
        start = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[n - 1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[n - 1]}")

        return ranges
