from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        for i in range(min_length):
            for s in strs:
                if strs[0][i] != s[i]:
                    return s[:i]

        return strs[0][:min_length]
