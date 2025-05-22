/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
  if (nums.length === 0) return [];

  let ans = [];
  let start = nums[0];
  let end = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === end + 1) end = nums[i];
    else {
      if (start === end) ans.push(start.toString());
      else ans.push(`${start}->${end}`);
      start = nums[i];
      end = nums[i];
    }
  }

  if (start === end) ans.push(start.toString());
  else ans.push(`${start}->${end}`);

  return ans;
};

// Time: O(n)
// Space: O(1)
