class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(sorted(nums)):
            if n not in d:
                d[n] = i
        
        ans = []
        for n in nums:
            ans.append(d[n])

        return ans

# Time: O(n log n)
# Space: O(n)