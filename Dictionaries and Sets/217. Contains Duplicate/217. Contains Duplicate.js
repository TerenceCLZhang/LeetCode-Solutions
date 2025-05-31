/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const sett = new Set(nums);
  return nums.length !== sett.size;
};

// Time: O(n)
// Space: O(n)
