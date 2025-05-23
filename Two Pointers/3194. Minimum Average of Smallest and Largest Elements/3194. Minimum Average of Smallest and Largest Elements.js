/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverage = function (nums) {
  nums.sort((a, b) => a - b);
  let min_average = Infinity;
  let l = 0;
  let r = nums.length - 1;

  while (l < r) {
    min_average = Math.min(min_average, (nums[l] + nums[r]) / 2);
    l++;
    r--;
  }

  return min_average;
};

// Time: O(n log n)
// Space: O(1)
