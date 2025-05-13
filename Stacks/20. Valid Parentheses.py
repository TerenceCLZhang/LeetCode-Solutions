class Solution:
    def isValid(self, s: str) -> bool:
        compliment = {")" : "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char not in compliment:
                stack.append(c)
            else:
                if not stack or stack[-1] != compliment[c]:
                    return False
                stack.pop()
        
        return not stack

# Time: O(n)
# Space: O(n)