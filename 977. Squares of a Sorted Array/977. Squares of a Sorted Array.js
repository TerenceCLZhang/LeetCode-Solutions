/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
  const squaredSorted = [];
  const n = nums.length;
  let left = 0;
  let right = n - 1;

  while (left <= right) {
    const leftSquared = nums[left] ** 2;
    const rightSquared = nums[right] ** 2;

    if (leftSquared > rightSquared) {
      squaredSorted.push(leftSquared);
      left++;
    } else {
      squaredSorted.push(rightSquared);
      right--;
    }
  }

  squaredSorted.reverse();

  return squaredSorted;
};
