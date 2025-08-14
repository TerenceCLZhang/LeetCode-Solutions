class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in parentheses:
                if not stack:
                    return False

                popped = stack.pop()
                if popped != parentheses[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
