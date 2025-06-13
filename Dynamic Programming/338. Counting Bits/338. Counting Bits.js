/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  ans = [0];
  for (let i = 1; i < n + 1; i++) {
    ans.push(ans[Math.floor(i / 2)] + (i % 2));
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
