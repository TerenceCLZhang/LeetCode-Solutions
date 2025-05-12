class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lo = 0
        hi = n - 1
        sorted_squares = []

        while lo <= hi:
            if abs(nums[lo]) < abs(nums[hi]):
                sorted_squares.append(nums[hi] ** 2)
                hi -= 1
            else:
                sorted_squares.append(nums[lo] ** 2)
                lo += 1

        # Reversing the array
        lo = 0
        hi = n - 1
        while lo < hi:
            sorted_squares[lo], sorted_squares[hi] = sorted_squares[hi], sorted_squares[lo]
            lo += 1
            hi -= 1

        return sorted_squares

# Time: O(n)
# Space: O(n)