from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for i in range(1, amount + 1):
            minn = float("inf")

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break

                minn = min(minn, dp[diff] + 1)

            dp[i] = minn

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]
