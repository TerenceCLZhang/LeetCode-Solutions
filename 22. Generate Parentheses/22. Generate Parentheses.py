from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, curr = [], []

        def backtrack(start, end):
            if len(curr) == n * 2:
                ans.append("".join(curr[:]))
                return

            if start < n:
                curr.append("(")
                backtrack(start + 1, end)
                curr.pop()

            if end < start:
                curr.append(")")
                backtrack(start, end + 1)
                curr.pop()

        backtrack(0, 0)
        return ans
