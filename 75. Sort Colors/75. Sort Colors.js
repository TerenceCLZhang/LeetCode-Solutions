/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let low = 0;
  let curr = 0;
  let high = nums.length - 1;

  while (curr <= high) {
    if (nums[curr] === 0) {
      [nums[low], nums[curr]] = [nums[curr], nums[low]];
      low++;
      curr++;
    } else if (nums[curr] === 1) {
      curr++;
    } else {
      [nums[curr], nums[high]] = [nums[high], nums[curr]];
      high--;
    }
  }
};
