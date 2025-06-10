/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let count = 1;
  let j = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) count++;
    else count = 1;

    if (count <= 2) {
      nums[j] = nums[i];
      j++;
    }
  }

  return j;
};

// Time: O(n)
// Space: O(1)
