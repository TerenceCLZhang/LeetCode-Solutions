class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        sett = set()
        for n in nums:
            if n in sett:
                sett.remove(n)
            else:
                sett.add(n)

        return len(sett) == 0

# Time: O(n)
# Space: O(n)
