/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function (s) {
  count = {};
  for (const char of s) {
    count[char] = (count[char] || 0) + 1;
  }

  let maxOdd = 0;
  let minEven = Infinity;

  for (const v of Object.values(count)) {
    if (v % 2 === 0) minEven = Math.min(minEven, v);
    else maxOdd = Math.max(maxOdd, v);
  }

  return maxOdd - minEven;
};

// Time: O(n)
// Space: O(1)
