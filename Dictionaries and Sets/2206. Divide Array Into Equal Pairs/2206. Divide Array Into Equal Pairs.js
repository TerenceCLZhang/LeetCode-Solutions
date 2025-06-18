/**
 * @param {number[]} nums
 * @return {boolean}
 */
var divideArray = function (nums) {
  sett = new Set();

  for (const n of nums) {
    if (sett.has(n)) sett.delete(n);
    else sett.add(n);
  }

  return sett.size === 0;
};

// Time: O(n)
// Space: O(n)
