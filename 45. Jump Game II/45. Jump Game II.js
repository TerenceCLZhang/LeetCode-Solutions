/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
  let ans = 0;
  let left = 0;
  let right = 0;

  while (right < nums.length - 1) {
    let farthest = 0;

    for (let i = left; i < right + 1; i++) {
      farthest = Math.max(farthest, nums[i] + i);
    }

    left = right + 1;
    right = farthest;
    ans++;
  }

  return ans;
};
