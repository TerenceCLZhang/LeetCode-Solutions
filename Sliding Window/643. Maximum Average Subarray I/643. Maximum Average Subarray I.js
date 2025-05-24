/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  let current_sum = nums.slice(0, k).reduce((a, c) => a + c, 0);
  let max_avg = current_sum / k;

  for (let i = k; i < nums.length; i++) {
    current_sum += nums[i] - nums[i - k];
    max_avg = Math.max(max_avg, current_sum / k);
  }

  return max_avg;
};

// Time: O(n)
// Space: O(1)
