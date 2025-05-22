class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for s in strs:
            min_length = min(min_length, len(s))
        
        for i in range(min_length):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return s[:i]
        
        return strs[0][:min_length]

# Time: O(n * m)
# Space: O(1)