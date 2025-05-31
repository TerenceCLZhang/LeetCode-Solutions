/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function (nums) {
  let ans = [];
  for (const n of nums) {
    let i = Math.abs(n);

    if (i === 999) i = 0;
    if (nums[i] === 0) nums[i] = 999;

    if (nums[i] < 0) ans.push(i);
    else nums[i] *= -1;
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
