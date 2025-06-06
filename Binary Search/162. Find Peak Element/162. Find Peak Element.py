class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (low + high) // 2
            left = mid == 0 or nums[mid] > nums[mid - 1]
            right = mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
            if left and right:
                return mid
            elif left:
                low = mid + 1
            else:
                high = mid - 1
        
# Time: O(log n)
# Space: O(1)