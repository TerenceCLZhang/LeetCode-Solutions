class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []

        def backtrack(openn, close):
            if openn == close == n:
                ans.append("".join(curr))
                return

            if openn < n:
                curr.append("(")
                backtrack(openn + 1, close)
                curr.pop()

            if close < openn:
                curr.append(")")
                backtrack(openn, close + 1)
                curr.pop()

        backtrack(0, 0)
        return ans
