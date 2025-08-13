/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const n = nums.length;
  const sums = [];

  for (let i = 0; i < n; i++) {
    if (nums[i] > 0) {
      break;
    }

    if (i !== 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = n - 1;

    while (left < right) {
      const summ = nums[i] + nums[left] + nums[right];
      if (summ === 0) {
        sums.push([nums[i], nums[left], nums[right]]);

        left++;
        right--;

        while (left < right && nums[left] === nums[left - 1]) {
          left++;
        }

        while (left < right && nums[right] === nums[right + 1]) {
          right--;
        }
      } else if (summ > 0) {
        right--;
      } else {
        left++;
      }
    }
  }

  return sums;
};
