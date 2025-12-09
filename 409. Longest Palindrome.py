class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        length = 0
        counter = Counter(s)

        for v in counter.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                odd = True

        return length if not odd else length + 1
