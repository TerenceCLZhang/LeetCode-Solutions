class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        closest = float("inf")
        ans = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == target:
                    return target

                diff = abs(target - summ)
                if diff < closest:
                    closest = diff
                    ans = summ

                if summ > target:
                    right -= 1
                else:
                    left += 1

        return ans
