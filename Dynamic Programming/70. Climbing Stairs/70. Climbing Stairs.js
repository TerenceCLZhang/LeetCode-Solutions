/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 2) return n;

  let prev2 = 1;
  let prev1 = 2;

  for (let i = 2; i < n; i++) {
    [prev2, prev1] = [prev1, prev2 + prev1];
  }

  return prev1;
};

// Time: O(n)
// Space: O(1)
