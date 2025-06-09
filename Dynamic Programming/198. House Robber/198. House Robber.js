/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (i === 1) nums[i] = Math.max(nums[i], nums[i - 1]);
    else nums[i] = Math.max(nums[i - 1], nums[i - 2] + nums[i]);
  }

  return nums.at(-1);
};
// Time: O(n)
// Space: O(1)
