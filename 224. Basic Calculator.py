class Solution:
    def calculate(self, s: str) -> int:
        curr_num = res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in "+-":
                res += sign * curr_num
                curr_num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append((res, sign))
                res = 0
                sign = 1
            elif char == ")":
                prev_res, prev_sign = stack.pop()
                res += sign * curr_num
                res = res * prev_sign + prev_res

                curr_num = 0

        return res + sign * curr_num
