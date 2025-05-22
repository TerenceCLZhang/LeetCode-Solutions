class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        c = 0
        for s in stones:
            if s in j:
                c += 1
        return c

# Time: O(n + m)
# Space: O(n)