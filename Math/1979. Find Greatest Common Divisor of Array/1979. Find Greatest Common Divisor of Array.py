class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        minn = min(nums)
        maxx = max(nums)
        
        return gcd(minn, maxx)

## Time: O(n)
# Space: O(1)