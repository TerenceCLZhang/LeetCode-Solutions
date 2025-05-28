/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min_price = Infinity;
  let max_profit = 0;

  for (const p of prices) {
    min_price = Math.min(min_price, p);
    max_profit = Math.max(max_profit, p - min_price);
  }

  return max_profit;
};

// Time: O(n)
// Space: O(1)
