/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  coins.sort((a, b) => a - b);

  for (let i = 1; i < amount + 1; i++) {
    let min = Infinity;

    for (const coin of coins) {
      const diff = i - coin;
      if (diff < 0) {
        break;
      }

      min = Math.min(min, dp[diff] + 1);
    }

    dp[i] = min;
  }

  return dp[amount] !== Infinity ? dp[amount] : -1;
};
