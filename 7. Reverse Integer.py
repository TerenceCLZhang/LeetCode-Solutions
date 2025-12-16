class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        is_neg = x < 0
        x = abs(x)

        while x > 0:
            ans *= 10
            last_digit = x % 10
            ans += last_digit

            if ans > 2 ** 31 - 1:
                return 0

            x //= 10

        return -ans if is_neg else ans
