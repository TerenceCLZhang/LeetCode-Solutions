/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function (nums) {
  if (nums.length <= 2) return -1;

  const minn = Math.min(...nums);
  const maxx = Math.max(...nums);

  for (const n of nums) {
    if (n !== minn && n !== maxx) return n;
  }
};

// Time: O(n)
// Space: O(1)
