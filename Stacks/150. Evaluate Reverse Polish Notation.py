class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == "+":
                    ans = val1 + val2
                elif token == "-":
                    ans = val1 - val2
                elif token == "*":
                    ans = val1 * val2
                else:
                    ans = int(val1 / val2)
                stack.append(ans)
            
        return stack.pop()

# Time: O(n)
# Space: O(n)