/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let ans = 0;
  for (let i = 0; i < 32; i++) {
    const bit = (n >> i) & 1;
    ans |= bit << (31 - i);
  }
  return ans >>> 0;
};

// Time: O(1)
// Space: O(1)
