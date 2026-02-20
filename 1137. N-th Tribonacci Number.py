class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        n1 = 0
        n2 = 1
        n3 = 1

        for _ in range(3, n + 1):
            n1, n2, n3 = n2, n3, n1 + n2 + n3

        return n3
