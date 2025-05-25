/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  let start = 0;
  let summ = 0;
  let min_length = Infinity;

  for (let i = 0; i < nums.length; i++) {
    summ += nums[i];

    while (summ >= target) {
      min_length = Math.min(min_length, i - start + 1);
      summ -= nums[start];
      start++;
    }
  }

  if (min_length === Infinity) return 0;
  return min_length;
};

// Time: O(n)
// Space: O(1)
