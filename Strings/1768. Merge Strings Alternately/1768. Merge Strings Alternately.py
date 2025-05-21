class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        max_length = max(l1, l2)
        ans = ""

        for i in range(max_length):
            if i < l1:
                ans += word1[i]
            if i < l2:
                ans += word2[i]
        
        return ans

# Time: O(n)
# Space: O(1)