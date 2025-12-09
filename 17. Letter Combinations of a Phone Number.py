class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        curr = []

        def backtrack(index):
            if index == len(digits):
                ans.append("".join(curr[:]))
                return

            for char in digit_letter_mapping[digits[index]]:
                curr.append(char)
                backtrack(index + 1)
                curr.pop()

        backtrack(0)
        return ans
