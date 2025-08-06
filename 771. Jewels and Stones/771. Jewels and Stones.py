class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        count = 0
        for stone in stones:
            if stone in j:
                count += 1
        return count
