import java.util.Arrays;

class Solution {

  public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, Integer.MAX_VALUE);
    dp[0] = 0;

    Arrays.sort(coins);

    for (int i = 1; i < amount + 1; i++) {
      int min = Integer.MAX_VALUE;

      for (int coin : coins) {
        int diff = i - coin;
        if (diff < 0) {
          break;
        }
        if (dp[diff] != Integer.MAX_VALUE) {
          min = Math.min(min, dp[diff] + 1);
        }
      }

      dp[i] = min;
    }

    return dp[amount] != Integer.MAX_VALUE ? dp[amount] : -1;
  }
}
