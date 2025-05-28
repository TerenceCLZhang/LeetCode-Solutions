/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function (nums) {
  let c = nums[0];
  for (const n of nums) {
    if (Math.abs(n) < Math.abs(c) || (Math.abs(n) == Math.abs(c) && n > c)) {
      c = n;
    }
  }
  return c;
};

// Time: O(n)
// Space: O(1)
