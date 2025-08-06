class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        max_length = max(l1, l2)
        merged = []

        for i in range(max_length):
            if i < l1:
                merged.append(word1[i])

            if i < l2:
                merged.append(word2[i])

        return "".join(merged)
