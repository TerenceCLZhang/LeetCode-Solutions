/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const unique = new Set(nums);
  let largest = 0;

  for (let n of unique) {
    if (!unique.has(n - 1)) {
      let current = 0;
      while (unique.has(n)) {
        current++;
        n++;
      }
      largest = Math.max(largest, current);
    }
  }

  return largest;
};
