/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  let minLength = Infinity;
  let currSum = 0;
  let left = 0;

  for (let i = 0; i < nums.length; i++) {
    currSum += nums[i];

    while (currSum >= target) {
      minLength = Math.min(minLength, i - left + 1);
      currSum -= nums[left];
      left++;
    }
  }

  return minLength < Infinity ? minLength : 0;
};
