class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{end}")
                    
                start = end = nums[i]

        if start == end:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{end}")

        return ans

# Time: O(n)
# Space: O(1)