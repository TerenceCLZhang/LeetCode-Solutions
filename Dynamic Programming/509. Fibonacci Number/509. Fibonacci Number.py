class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, curr + prev
        
        return curr

# Time: O(n)
# Space: O(1)