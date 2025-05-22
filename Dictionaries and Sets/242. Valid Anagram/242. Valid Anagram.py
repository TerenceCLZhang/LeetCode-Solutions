class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter

# Time: O(n)
# Space: O(n)
# Where n is the length of the longest word