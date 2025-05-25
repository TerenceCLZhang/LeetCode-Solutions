/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  const sortedNums = nums.slice().sort((a, b) => a - b);
  let numsLess = {};
  for (let i = 0; i < sortedNums.length; i++) {
    if (!(sortedNums[i] in numsLess)) numsLess[sortedNums[i]] = i;
  }

  let ans = [];
  for (let n of nums) ans.push(numsLess[n]);
  return ans;
};

// Time: O(n log n)
// Space: O(n)