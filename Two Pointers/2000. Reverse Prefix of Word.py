class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        r = word.find(ch)

        if r == -1:
            return word

        word = list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return "".join(word)


# Time: O(n)
# Space: O(n)