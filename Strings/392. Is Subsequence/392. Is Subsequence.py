class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        if len(s) > len(t):
            return False

        s_idx = t_idx = 0
        while t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
            t_idx += 1
        
        return False
                
# Time: O(n)
# Space: O(1)