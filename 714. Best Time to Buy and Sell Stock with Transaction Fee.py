class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        holding = 0
        not_holding = 0

        for i in range(n - 1, -1, -1):
            holding = max(holding, prices[i] - fee + not_holding)
            not_holding = max(not_holding, -prices[i] + holding)

        return not_holding
