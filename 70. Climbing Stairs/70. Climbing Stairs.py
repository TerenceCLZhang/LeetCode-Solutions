class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        num1 = 1
        num2 = 2

        for _ in range(3, n + 1):
            num1, num2 = num2, num1 + num2

        return num2
