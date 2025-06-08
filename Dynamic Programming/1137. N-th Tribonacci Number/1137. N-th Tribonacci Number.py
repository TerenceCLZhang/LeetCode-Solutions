class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        prev2 = 0
        prev1 = 1
        curr = 1

        for _ in range(3, n + 1):
            summ = prev2 + prev1 + curr
            [prev2, prev1, curr] = [prev1, curr, summ]

        return curr

# Time: O(n)
# Space: O(1)