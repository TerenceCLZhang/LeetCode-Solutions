/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let currentElement = null;
  let count = 0;

  for (const n of nums) {
    if (count <= 0) {
      currentElement = n;
    }

    if (currentElement === n) {
      count++;
    } else {
      count--;
    }
  }

  return currentElement;
};
