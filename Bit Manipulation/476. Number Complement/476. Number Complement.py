class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = len(bin(num)[2:])
        max_num = 2 ** num_bits - 1
        return num ^ max_num

# Time: O(1)
# Space: O(1)