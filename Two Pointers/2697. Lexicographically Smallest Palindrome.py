class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                smaller = min(s[l], s[r])
                s[l] = s[r] = smaller
                
            l += 1
            r -= 1
        
        return "".join(s)

# Time: O(n)
# Space: O(n)