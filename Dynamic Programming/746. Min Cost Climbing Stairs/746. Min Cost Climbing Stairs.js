/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  for (let i = 2; i < cost.length; i++) {
    cost[i] = Math.min(cost[i - 1] + cost[i], cost[i - 2] + cost[i]);
  }

  return Math.min(cost.at(-1), cost.at(-2));
};

// Time: O(n)
// Space: O(1)
