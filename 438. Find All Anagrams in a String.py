class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        ans = []
        s_length, p_length = len(s), len(p)
        s_counter, p_counter = {}, {}

        for i in range(p_length):
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            p_counter[p[i]] = 1 + p_counter.get(p[i], 0)

        if s_counter == p_counter:
            ans.append(0)

        for i in range(p_length, s_length):
            s_counter[s[i - p_length]] -= 1
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)

            if s_counter[s[i - p_length]] == 0:
                del s_counter[s[i - p_length]]

            if s_counter == p_counter:
                ans.append(i - p_length + 1)

        return ans
