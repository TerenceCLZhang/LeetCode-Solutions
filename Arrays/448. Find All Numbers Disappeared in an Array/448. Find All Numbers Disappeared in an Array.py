class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])
        
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
        
        return ans

# Time: O(n)
# Space: O(1)