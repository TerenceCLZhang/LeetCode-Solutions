/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  let num1 = 0,
    num2 = 0;

  for (let i = 2; i < cost.length + 1; i++) {
    [num1, num2] = [num2, Math.min(num1 + cost[i - 2], num2 + cost[i - 1])];
  }

  return num2;
};
