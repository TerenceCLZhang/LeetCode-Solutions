/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const actual_sum = nums.reduce((a, c) => a + c, 0);
  const expected_sum = (nums.length * (nums.length + 1)) / 2;
  return expected_sum - actual_sum;
};

// Time: O(n)
// Space: O(1)
