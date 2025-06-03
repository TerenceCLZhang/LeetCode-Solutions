# Brian Kernighan’s Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans

# Time: O(k)
# Space: O(1)
# Where k is the number of 1 bits