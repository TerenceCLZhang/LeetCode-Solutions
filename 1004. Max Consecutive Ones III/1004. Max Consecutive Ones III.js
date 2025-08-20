/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let numFlipped = 0;
  let left = 0;
  let maxLength = 0;

  for (let curr = 0; curr < nums.length; curr++) {
    if (nums[curr] === 0) {
      numFlipped++;
    }

    while (numFlipped > k) {
      if (nums[left] === 0) {
        numFlipped--;
      }
      left += 1;
    }

    const currLength = curr - left + 1;
    maxLength = Math.max(maxLength, currLength);
  }

  return maxLength;
};
