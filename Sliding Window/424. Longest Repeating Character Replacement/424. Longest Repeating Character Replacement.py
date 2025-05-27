class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = [0] * 26
        longest = 0
        l = 0

        for r in range(len(s)):
            characters[ord(s[r]) - ord("A")] += 1

            while r - l + 1 - max(characters) > k:
                characters[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
        
# Time: O(n)
# Space: O(1)