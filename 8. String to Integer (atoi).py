class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if s == "":
            return 0

        sign = 1
        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        num = 0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            num = 10 * num + int(s[i])

        num *= sign
        num = min(num, 2 ** 31 - 1)
        num = max(-2 ** 31, num)

        return num
