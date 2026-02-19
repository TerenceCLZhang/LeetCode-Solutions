class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        potions.sort()

        for s in spells:
            left = 0
            right = len(potions) - 1

            while left <= right:
                mid = (left + right) // 2
                pair = potions[mid] * s

                if pair < success:
                    left = mid + 1
                else:
                    right = mid - 1

            ret.append(len(potions) - left)

        return ret
