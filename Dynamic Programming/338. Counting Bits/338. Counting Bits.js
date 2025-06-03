/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  ans = new Array(n + 1).fill(0);
  for (let i = 1; i < n + 1; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
