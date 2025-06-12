/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function (nums) {
  let maxDiff = 0;

  for (let i = 0; i < nums.length; i++) {
    maxDiff = Math.max(maxDiff, Math.abs(nums.at(i) - nums.at(i - 1)));
  }

  return maxDiff;
};

// Time: O(n)
// Space: O(1)
