class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s_len, t_len = len(s), len(t)

        if s_len > t_len:
            return False

        s_pointer = 0

        for t_pointer in range(t_len):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1

            if s_pointer == s_len:
                return True

        return False
