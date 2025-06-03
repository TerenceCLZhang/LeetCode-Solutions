/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  let l = 0;
  let r = nums.reduce((a, b) => a + b);

  for (let i = 0; i < nums.length; i++) {
    r -= nums[i];
    if (r == l) return i;
    l += nums[i];
  }

  return -1;
};

// Time: O(n)
// Space: O(1)
