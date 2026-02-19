class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            
            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid