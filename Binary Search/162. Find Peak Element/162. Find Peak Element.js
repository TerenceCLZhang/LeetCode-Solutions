/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  let low = 0;
  let high = nums.length;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const left = mid === 0 || nums[mid] > nums[mid - 1];
    const right = mid === nums.length - 1 || nums[mid] > nums[mid + 1];
    if (left && right) return mid;
    else if (left) low = mid + 1;
    else high = mid - 1;
  }
};

// Time: O(log n)
// Space: O(1)
