class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []

        def backtrack(start):
            if start >= len(s):
                ans.append(curr[:])
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start: i + 1]):
                    curr.append(s[start: i + 1])
                    backtrack(i + 1)
                    curr.pop()

        def is_palindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        backtrack(0)
        return ans
