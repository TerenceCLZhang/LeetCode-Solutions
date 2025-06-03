/**
 * @param {number} n
 * @return {number}
 */

// Brian Kernighan’s Algorithm
var hammingWeight = function (n) {
  let ans = 0;
  while (n) {
    n &= n - 1;
    ans++;
  }
  return ans;
};

// Time: O(k)
// Space: O(1)
// Where k is the number of 1 bits
