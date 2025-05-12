class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lo = 0
        hi = n - 1

        while lo < hi:
            summ = numbers[lo] + numbers[hi]
            if summ == target:
                return (lo + 1, hi + 1)
            elif summ > target:
                hi -= 1
            else:
                lo += 1

# Time: O(n)
# Space: O(1)