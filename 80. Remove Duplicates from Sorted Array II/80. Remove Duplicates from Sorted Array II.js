/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  const n = nums.length;

  if (n < 3) {
    return n;
  }

  let left = 2;
  for (let right = 2; right < n; right++) {
    if (nums[right] != nums[left - 2]) {
      nums[left] = nums[right];
      left++;
    }
  }

  return left;
};
