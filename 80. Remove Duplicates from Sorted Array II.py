class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        j = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 0

            if count < 2:
                nums[j] = nums[i]
                j += 1

        return j
