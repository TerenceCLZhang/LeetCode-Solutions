class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / k

        for i in range(k, len(nums)):
            curr_sum -= nums[i - k]
            curr_sum += nums[i]

            curr_avg = curr_sum / k
            max_avg = max(curr_avg, max_avg)
        
        return max_avg

# Time: O(n)
# Space: O(1)