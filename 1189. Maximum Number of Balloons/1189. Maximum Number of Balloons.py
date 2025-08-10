class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for char in text:
            if char in letters:
                letters[char] += 1

        return min(letters["b"], letters["a"], letters["l"] // 2, letters["o"] // 2, letters["n"])
