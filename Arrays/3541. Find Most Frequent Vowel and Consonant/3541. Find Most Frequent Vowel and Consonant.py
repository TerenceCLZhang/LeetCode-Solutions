class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = [0] * 26
        consonants = [0] * 26

        for char in s:
            i = ord(char) - ord("a")
            if char in "aeiou":
                vowels[i] += 1
            else:
                consonants[i] += 1
        
        return max(vowels) + max(consonants)

# Time: O(n)
# Space: O(1)