class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            idx = abs(n) - 1
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] *= -1
        
        return ans

# Time: O(n)
# Space: O(1)