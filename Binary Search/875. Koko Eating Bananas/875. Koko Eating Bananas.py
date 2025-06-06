class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while (low <= high):
            k = (low + high) // 2
            curr_time = 0
            for b in piles:
                curr_time += ceil(b / k)

            if curr_time <= h:
                high = k - 1
            else:
                low = k + 1
        
        return low

# Time: O(n log max(piles))
# Space: O(1)