/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  const n = nums.length;
  let target = n - 1;

  for (let i = n - 1; i > -1; i--) {
    if (i + nums[i] >= target) {
      target = i;
    }
  }

  return target === 0;
};
