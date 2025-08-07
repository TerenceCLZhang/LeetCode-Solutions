class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        n = len(s)
        m = len(t)

        if n > m:
            return False

        i = 0
        for j in range(m):
            if s[i] == t[j]:
                i += 1

            if i == n:
                return True

        return False
