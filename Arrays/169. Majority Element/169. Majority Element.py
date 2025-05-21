# Boyer-Moore Majority Vote Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_max = None
        count = 0
        for n in nums:
            if n == current_max:
                count += 1
            elif count == 0:
                current_max = n
                count = 1
            else:
                count -= 1
        return current_max

# Time: O(n)
# Space: O(1)