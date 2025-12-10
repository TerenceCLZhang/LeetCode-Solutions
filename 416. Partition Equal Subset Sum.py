class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = set([0])

        for n in nums:
            temp_dp = dp.copy()
            for s in dp:
                temp_dp.add(s + n)

            if target in dp:
                return True

            dp = temp_dp

        return False
