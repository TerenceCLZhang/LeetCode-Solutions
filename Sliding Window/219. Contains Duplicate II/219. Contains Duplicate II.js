/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  let sett = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (sett.has(nums[i])) return true;
    sett.add(nums[i]);
    if (sett.size > k) sett.delete(nums[i - k]);
  }
  return false;
};

// Time: O(n)
// Space: O(k)
