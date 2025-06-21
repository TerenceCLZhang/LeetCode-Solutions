/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  const findFirst = () => {
    let l = 0,
      r = nums.length - 1;
    let index = -1;
    while (l <= r) {
      const m = Math.floor((l + r) / 2);
      if (nums[m] < target) l = m + 1;
      else r = m - 1;
      if (nums[m] === target) index = m;
    }
    return index;
  };

  const findLast = () => {
    let l = 0,
      r = nums.length - 1;
    let index = -1;
    while (l <= r) {
      const m = Math.floor((l + r) / 2);
      if (nums[m] > target) r = m - 1;
      else l = m + 1;
      if (nums[m] === target) index = m;
    }
    return index;
  };

  return [findFirst(), findLast()];
};

// Time: O(log n)
// Space: O(1)
