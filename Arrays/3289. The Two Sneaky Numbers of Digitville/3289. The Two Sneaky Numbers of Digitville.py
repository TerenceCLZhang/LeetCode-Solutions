class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:   
        ans = []
        for n in nums:
            i = abs(n)
            if i == 999:
                i = 0
            
            if nums[i] == 0:
                nums[i] = 999
            
            if nums[i] < 0:
                ans.append(i)
            
            else:
                nums[i] *= -1

        return ans

# Time: O(n)
# Space: O(1)