from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end1 = m - 1
        end2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if end2 < 0:
                break
            elif end1 >= 0 and nums1[end1] > nums2[end2]:
                nums1[i] = nums1[end1]
                end1 -= 1
            else:
                nums1[i] = nums2[end2]
                end2 -= 1
