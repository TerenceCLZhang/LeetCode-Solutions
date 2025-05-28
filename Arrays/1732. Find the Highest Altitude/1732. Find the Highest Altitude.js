/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  let curr_a = 0;
  let max_a = 0;

  for (const g of gain) {
    curr_a += g;
    max_a = Math.max(max_a, curr_a);
  }

  return max_a;
};

// Time: O(n)
// Space: O(1)
