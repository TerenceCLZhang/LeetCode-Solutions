/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let low = 1;
  let high = num;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const square = mid * mid;

    if (square === num) {
      return true;
    } else if (square > num) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return false;
};
