from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == target:
                    return summ

                if abs(target - summ) < abs(target - closest):
                    closest = summ

                if summ > target:
                    right -= 1
                else:
                    left += 1

        return closest
