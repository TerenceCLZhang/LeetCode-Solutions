class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float("inf")
        for n in nums:
            if abs(n) < abs(closest):
                closest = n

        if closest < 0 and abs(closest) in nums:
            closest *= -1

        return closest
