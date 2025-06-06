/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let ans = 0;
  for (const n of nums) ans ^= n;
  return ans;
};

// Time: O(n)
// Space: O(1)