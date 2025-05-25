class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = -float("inf")

        for n in nums:
            if n in (first_max, second_max, third_max):
                continue

            if n > first_max:
                first_max, second_max, third_max = n, first_max, second_max
            elif n > second_max:
                second_max, third_max = n, second_max
            elif n > third_max:
                third_max = n
        
        return third_max if third_max != -float("inf") else first_max

# Time: O(n)
# Space: O(1)