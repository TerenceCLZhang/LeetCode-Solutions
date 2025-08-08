/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
  if (nums.length == 0) {
    return [];
  }

  const summaryRanges = [];
  let start = 0;

  for (let i = 1; i < nums.length + 1; i++) {
    if (i == nums.length || nums[i] !== nums[i - 1] + 1) {
      if (start === i - 1) {
        summaryRanges.push(`${nums[start]}`);
      } else {
        summaryRanges.push(`${nums[start]}->${nums[i - 1]}`);
      }

      start = i;
    }
  }

  return summaryRanges;
};
