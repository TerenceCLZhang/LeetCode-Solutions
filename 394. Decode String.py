class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n

                stack.append(int(n) * substring)

        return "".join(stack)
