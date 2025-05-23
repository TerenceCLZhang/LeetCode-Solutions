/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let l = 0;
  let r = numbers.length - 1;

  while (l < r) {
    const summ = numbers[l] + numbers[r];
    if (summ === target) return [l + 1, r + 1];
    else if (summ > target) r--;
    else l++;
  }
};

// Time: O(n)
// Space: O(1)
