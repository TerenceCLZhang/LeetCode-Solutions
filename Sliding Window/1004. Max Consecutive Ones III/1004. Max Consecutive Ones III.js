/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let longest = 0;
  let num_zeros = 0;
  let l = 0;

  for (let r = 0; r < nums.length; r++) {
    if (nums[r] === 0) num_zeros++;

    while (num_zeros > k) {
      if (nums[l] === 0) num_zeros--;
      l++;
    }

    longest = Math.max(longest, r - l + 1);
  }

  return longest;
};

// Time: O(n)
// Space: O(1)
