class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        longest = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest

# Time: O(n)
# Space: O(1)