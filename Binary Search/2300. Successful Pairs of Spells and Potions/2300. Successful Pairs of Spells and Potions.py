class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for s in spells:
            low = 0
            high = len(potions) - 1
            index = len(potions)
            
            while low <= high:
                mid = (low + high) // 2
                if s * potions[mid] >= success:
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1
        
            ans.append(len(potions) - index)

        return ans

# Time: O(m log m + n log m)
# Space: O(1)