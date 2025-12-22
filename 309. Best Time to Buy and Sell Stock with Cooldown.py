class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(index, buying):
            if index >= len(prices):
                return 0

            if (index, buying) in cache:
                return cache[(index, buying)]

            if buying:
                buy = dfs(index + 1, False) - prices[index]
                cooldown = dfs(index + 1, True)
                cache[(index, buying)] = max(buy, cooldown)
            else:
                sell = dfs(index + 2, True) + prices[index]
                cooldown = dfs(index + 1, False)
                cache[(index, buying)] = max(sell, cooldown)

            return cache[(index, buying)]

        return dfs(0, True)
