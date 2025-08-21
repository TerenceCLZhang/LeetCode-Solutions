class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = [0] * 26
        max_length = 0
        max_count = 0
        left = 0

        for i in range(len(s)):
            alphabet_index = ord(s[i]) - ord("A")
            alphabet[alphabet_index] += 1
            max_count = max(max_count, alphabet[alphabet_index])

            while i - left + 1 - max_count > k:
                alphabet[ord(s[left]) - ord("A")] -= 1
                left += 1

            curr_length = i - left + 1
            max_length = max(max_length, curr_length)

        return max_length
