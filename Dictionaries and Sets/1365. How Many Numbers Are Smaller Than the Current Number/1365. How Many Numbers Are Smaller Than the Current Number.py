class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictt = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dictt:
                dictt[n] = i 
        
        ans = []
        for n in nums:
            ans.append(dictt[n])
        
        return ans

# Time: O(n log n)
# Space: O(n)