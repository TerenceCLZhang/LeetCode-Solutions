# Memoization Solution

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         cache = {}

#         def dfs(index, total):
#             if total == amount:
#                 return 1

#             if index >= len(coins) or total > amount:
#                 return 0

#             if (index, total) in cache:
#                 return cache[(index, total)]

#             cache[(index, total)] = dfs(index, total + coins[index]) + dfs(index + 1, total)
#             return cache[(index, total)]

#         return dfs(0, 0)


# 2D DP Solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for coin_i in range(1, n + 1):
            for amount_i in range(1, amount + 1):
                a = dp[coin_i - 1][amount_i]
                new_amount_i = amount_i - coins[coin_i - 1]
                if new_amount_i >= 0:
                    a += dp[coin_i][new_amount_i]
                dp[coin_i][amount_i] = a

        return dp[n][amount]
