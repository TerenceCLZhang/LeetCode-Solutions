class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            small, large = nums1, nums2
        else:
            small, large = nums2, nums1
        
        sett = set(small)
        ans = []
        for n in large:
            if n in sett:
                ans.append(n)
                sett.remove(n)
        return ans


# Time: O(n + m)
# Space: O(min(n, m))
# Where n is the length of num1 and m is the length of num2