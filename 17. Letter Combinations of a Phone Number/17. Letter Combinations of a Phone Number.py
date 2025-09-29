from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        ans, curr = [], []

        def backtrack(i):
            if len(curr) == n:
                ans.append("".join(curr))
                return

            for c in digits_map[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return ans
