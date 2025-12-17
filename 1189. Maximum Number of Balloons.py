class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapping = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for char in text:
            if char in mapping:
                mapping[char] += 1

        return min(mapping["b"], mapping["a"], mapping["l"] // 2, mapping["o"] // 2, mapping["n"])
