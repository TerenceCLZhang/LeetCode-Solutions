class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)

        for l in ransomNote:
            if l not in letters:
                return False

            letters[l] -= 1
            if letters[l] <= 0:
                del letters[l]

        return True
