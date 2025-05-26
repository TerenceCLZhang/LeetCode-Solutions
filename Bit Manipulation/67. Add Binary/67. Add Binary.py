class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            with_carry = (a & b) << 1
            a, b = without_carry, with_carry
        
        return bin(a)[2:]

# Time: O(a + b)
# Space: O(1)