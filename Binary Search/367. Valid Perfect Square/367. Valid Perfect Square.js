/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let l = 0;
  let r = num;
  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    const s = m * m;
    if (s === num) return true;
    else if (s > num) r = m - 1;
    else l = m + 1;
  }
  return false;
};

// Time: O(log n)
// Space: O(1)
