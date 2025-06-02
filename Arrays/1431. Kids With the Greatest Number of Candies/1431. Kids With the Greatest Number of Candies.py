class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxx = max(candies)
        for c in candies:
            extra = c + extraCandies
            if extra >= maxx:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            
# Time: O(n)
# Space: O(1)