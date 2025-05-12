class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        lo = 0
        hi = n - 1
        
        while l <= hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

# Time: O(n)
# Space: O(1)