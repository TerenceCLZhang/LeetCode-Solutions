class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))

        prefix = ""
        for i in range(min_len):
            for s in strs:
                if strs[0][i] != s[i]:
                    return prefix
            prefix += strs[0][i]

        return prefix
