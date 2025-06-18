class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0

        for char in s:
            if char == "(":
                if depth > 0:
                    ans.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(char)

        return "".join(ans)

# Time: O(n)
# Space: O(n)
