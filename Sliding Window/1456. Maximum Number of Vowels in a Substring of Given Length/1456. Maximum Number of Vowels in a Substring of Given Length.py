class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        num_vowels = 0

        for char in s[:k]:
            if char in vowels:
                num_vowels += 1

        max_vowels = num_vowels
        
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                num_vowels -= 1
            if s[i] in vowels:
                num_vowels += 1
            
            max_vowels = max(max_vowels, num_vowels)
        
        return max_vowels

# Time: O(n)
# Space: O(1)