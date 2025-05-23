/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var countPairs = function (nums, target) {
  nums.sort((a, b) => a - b);
  let l = 0;
  let r = nums.length - 1;
  let pairs = 0;

  while (l < r) {
    if (nums[l] + nums[r] < target) {
      pairs += r - l;
      l++;
    } else {
      r--;
    }
  }

  return pairs;
};

// Time: O(n log n)
// Space: O(1)
