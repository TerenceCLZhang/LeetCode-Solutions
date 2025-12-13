class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob(arr):
            if len(arr) == 1:
                return arr[0]

            prev2 = prev1 = 0

            for n in arr:
                not_rob = prev1
                rob = n + prev2
                prev2, prev1 = prev1, max(not_rob, rob)

            return prev1

        return max(rob(nums[:n - 1]), rob(nums[1:]))
