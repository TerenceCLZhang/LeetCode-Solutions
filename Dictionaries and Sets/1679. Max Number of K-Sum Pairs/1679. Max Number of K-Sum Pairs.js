/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {
  let c = {};
  let ops = 0;

  for (const n of nums) {
    const compliment = k - n;
    if (c[compliment] > 0) {
      c[compliment]--;
      ops++;
    } else c[n] = (c[n] || 0) + 1;
  }

  return ops;
};

// Time: O(n)
// Space: O(n)
