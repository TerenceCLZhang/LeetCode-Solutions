/**
 * @param {number[]} nums
 * @return {number}
 */

// Boyer-Moore Majority Vote Algorithm
var majorityElement = function (nums) {
  let currentMax = -Infinity;
  let count = 0;

  for (let n of nums) {
    if (n === currentMax) {
      count++;
    } else if (count === 0) {
      currentMax = n;
      count = 1;
    } else {
      count--;
    }
  }

  return currentMax;
};

// Time: O(n)
// Space: O(1)
