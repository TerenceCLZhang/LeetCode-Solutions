class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        curr = 0
        prev2 = 0
        prev1 = 1

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr

# Time: O(n)
# Space: O(1)