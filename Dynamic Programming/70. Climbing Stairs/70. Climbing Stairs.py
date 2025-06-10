class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2

        for _ in range(2, n):
            prev2, prev1 = prev1, prev2 + prev1
        
        return prev1

# Time: O(n)
# Space: O(1)