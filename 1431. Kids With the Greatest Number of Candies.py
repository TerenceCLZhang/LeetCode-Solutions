class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        ans = [c + extraCandies >= curr_max for c in candies]
        return ans
