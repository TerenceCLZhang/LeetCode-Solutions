class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(i, curr):
            if len(curr) == len(s):
                ans.append(curr)
                return
            
            if s[i].isalpha():
                backtrack(i + 1, curr + s[i].lower())
                backtrack(i + 1, curr + s[i].upper())
            else:
                backtrack(i + 1, curr + s[i])

        backtrack(0, "")
        return ans