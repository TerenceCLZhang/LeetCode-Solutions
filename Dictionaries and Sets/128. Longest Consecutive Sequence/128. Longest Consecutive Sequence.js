/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const sett = new Set(nums);
  let longest = 0;

  for (let n of sett) {
    if (!sett.has(n - 1)) {
      let curr = n;
      let curr_length = 1;
      while (sett.has(curr + 1)) {
        curr++;
        curr_length++;
      }
      longest = Math.max(longest, curr_length);
    }
  }

  return longest;
};

// Time: O(n)
// Space: O(n)
