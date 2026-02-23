class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_n = {}

        for i, n in enumerate(nums):
            if n not in seen_n:
                seen_n[n] = i
            else:
                if abs(i - seen_n[n]) <= k:
                    return True
                seen_n[n] = i

        return False
