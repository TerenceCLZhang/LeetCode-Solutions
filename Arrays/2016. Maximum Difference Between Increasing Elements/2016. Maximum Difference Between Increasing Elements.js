/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function (nums) {
  let max_diff = -1;
  let min_element = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === min_element) continue;

    if (nums[i] < min_element) min_element = nums[i];
    else max_diff = Math.max(max_diff, nums[i] - min_element);
  }

  return max_diff;
};

// Time: O(n)
// Space: O(1)
