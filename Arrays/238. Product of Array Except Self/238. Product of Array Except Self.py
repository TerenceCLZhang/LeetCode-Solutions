class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        l_mul = 1
        for n in nums:
            ans.append(l_mul)
            l_mul *= n
        
        r_mul = 1
        for i in range(len(nums) - 1, - 1, - 1):
            ans[i] *= r_mul
            r_mul *= nums[i]
        
        return ans

# Time: O(n)
# Space: O(1)