/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
  let ans = [];

  for (let i = 0; i < nums.length; i++) {
    const idx = Math.abs(nums[i]) - 1;
    nums[idx] = -1 * Math.abs(nums[idx]);
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) ans.push(i + 1);
  }

  return ans;
};

// Time: O(n)
// Space: O(1)
