class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = minn = maxx = nums[0]

        for i in range(1, len(nums)):
            temp_minn = minn
            minn = min(nums[i], minn * nums[i], maxx * nums[i])
            maxx = max(nums[i], maxx * nums[i], temp_minn * nums[i])
            max_prod = max(max_prod, maxx)
            
        return max_prod