class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i, word in enumerate(words):
            word = list(word)
            l = 0
            r = len(word) - 1

            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            
            words[i] = "".join(word)
        
        return " ".join(words)
        
# Time: O(n)
# Space: O(n)