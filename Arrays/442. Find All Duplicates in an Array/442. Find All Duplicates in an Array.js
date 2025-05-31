/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function (nums) {
  ans = [];
  for (let i = 0; i < nums.length; i++) {
    const idx = Math.abs(nums[i]) - 1;
    if (nums[idx] < 0) ans.push(idx + 1);
    else nums[idx] *= -1;
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
