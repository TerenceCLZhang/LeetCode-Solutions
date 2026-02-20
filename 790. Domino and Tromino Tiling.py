class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n <= 1:
            return 1
        elif n == 2:
            return 2
        
        prev2, prev1, curr = 1, 1, 2
        for _ in range(3, n + 1):
            prev2, prev1, curr = prev1, curr, 2 * curr + prev2
        
        return curr % MOD