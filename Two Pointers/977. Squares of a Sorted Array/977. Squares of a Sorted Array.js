/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
  let ans = [];
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    const low_squared = nums[l] ** 2;
    const high_squared = nums[r] ** 2;
    if (low_squared > high_squared) {
      ans.push(low_squared);
      l++;
    } else {
      ans.push(high_squared);
      r--;
    }
  }

  return ans.reverse();
};

// Time: O(n)
// Space: O(n)