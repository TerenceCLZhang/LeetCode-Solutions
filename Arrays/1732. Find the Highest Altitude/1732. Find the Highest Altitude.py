class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_a = 0
        max_a = 0

        for g in gain:
            curr_a += g
            max_a = max(max_a, curr_a)
        
        return max_a

# Time: O(n)
# Space: O(1)