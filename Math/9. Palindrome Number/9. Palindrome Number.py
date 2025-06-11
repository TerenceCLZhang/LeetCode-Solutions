class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10
        
        return x == half or x == half // 10

# Time: O(log x)
# Space: O(1)