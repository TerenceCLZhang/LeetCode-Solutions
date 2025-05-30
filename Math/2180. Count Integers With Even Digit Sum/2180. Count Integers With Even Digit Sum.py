class Solution:
    def countEven(self, num: int) -> int:
        def check_sum_even(num):
            summ = 0
            while num > 0:
                summ += num % 10
                num //= 10
            return summ % 2 == 0

        count = 0
        for n in range(1, num + 1):
            if check_sum_even(n):
                count += 1
        
        return count

# Time: O(n log n)
# Space: O(1)