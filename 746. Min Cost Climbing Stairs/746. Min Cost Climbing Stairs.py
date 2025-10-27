from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num1 = 0
        num2 = 0

        for i in range(2, len(cost) + 1):
            num1, num2 = num2, min(num1 + cost[i - 2], num2 + cost[i - 1])

        return num2
