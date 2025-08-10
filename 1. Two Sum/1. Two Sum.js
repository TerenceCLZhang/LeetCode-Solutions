/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const complement = new Map();
  for (let i = 0; i < nums.length; i++) {
    const needed = target - nums[i];
    if (complement.has(needed)) {
      return [complement.get(needed), i];
    }
    complement.set(nums[i], i);
  }
};
