/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const summ = numbers[left] + numbers[right];
    if (summ === target) {
      return [left + 1, right + 1];
    } else if (summ > target) {
      right--;
    } else {
      left++;
    }
  }
};
