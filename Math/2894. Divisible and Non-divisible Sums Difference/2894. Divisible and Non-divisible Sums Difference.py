class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for n in range(1, n + 1):
            if n % m == 0:
                num2 += n
            else:
                num1 += n

        return num1 - num2

# Time: O(n)
# Space: O(1)
