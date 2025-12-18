class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_neg = num < 0
        num = abs(num)
        ans = []

        while num > 0:
            remainder = num % 7
            ans.append(str(remainder))
            num //= 7

        if is_neg:
            ans.append("-")

        ans.reverse()
        return "".join(ans)
