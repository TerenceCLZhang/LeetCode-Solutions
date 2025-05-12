class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lo = 0
        hi = n - 1
        
        while lo <= hi:
            if not s[lo].isalnum():
                lo += 1
                continue

            if not s[hi].isalnum():
                hi -= 1
                continue
            
            if s[lo].lower() != s[hi].lower():
                return False
            
            lo += 1
            hi -= 1
        
        return True

# Time: O(n)
# Space: O(1)