/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
  let first_max = -Infinity;
  let second_max = -Infinity;
  let third_max = -Infinity;

  for (let n of nums) {
    if ([first_max, second_max, third_max].includes(n)) continue;

    if (n > first_max) {
      third_max = second_max;
      second_max = first_max;
      first_max = n;
    } else if (n > second_max) {
      third_max = second_max;
      second_max = n;
    } else if (n > third_max) {
      third_max = n;
    }
  }

  if (third_max === -Infinity) return first_max;
  return third_max;
};

// Time: O(n)
// Space: O(1)
