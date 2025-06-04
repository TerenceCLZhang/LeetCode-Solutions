class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_string = ""
                while stack[-1] != "[":
                    curr_string = stack.pop() + curr_string
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * curr_string)
            
        return "".join(stack)
            
# Time: O(L)
# Space: O(L)
# Where L is the length of the decided string