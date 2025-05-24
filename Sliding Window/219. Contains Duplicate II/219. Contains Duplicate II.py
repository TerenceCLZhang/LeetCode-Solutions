class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett = set()
        for i, n in enumerate(nums):
            if n in sett:
                return True
            sett.add(n)
            if len(sett) > k:
                sett.remove(nums[i - k])
        return False

# Time: O(n)
# Space: O(k)