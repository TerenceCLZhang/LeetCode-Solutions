class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l1, l2 = len(word1), len(word2)

        for i in range(min(l1, l2)):
            merged += word1[i] + word2[i]

        if l1 > l2:
            merged += word1[l2:]
        else:
            merged += word2[l1:]

        return merged
