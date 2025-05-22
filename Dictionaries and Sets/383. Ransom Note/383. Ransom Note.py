from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        
        for c in ransomNote:
            if c not in letters:
                return False
            if letters[c] == 1:
                del letters[c]
            else:
                letters[c] -= 1
        
        return True

# Time: O(n + m)
# Space: O(n)