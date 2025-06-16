class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_element = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == min_element:
                continue

            if nums[i] < min_element:
                min_element = nums[i]
            else:
                max_diff = max(max_diff, nums[i] - min_element)
        
        return max_diff

# Time: O(n)
# Space: O(1)