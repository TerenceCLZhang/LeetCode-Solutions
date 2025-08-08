/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (const p of prices) {
    if (p < minPrice) {
      minPrice = p;
    } else {
      maxProfit = Math.max(maxProfit, p - minPrice);
    }
  }

  return maxProfit;
};
