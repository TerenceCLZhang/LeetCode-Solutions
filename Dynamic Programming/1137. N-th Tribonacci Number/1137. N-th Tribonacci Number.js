/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  if (n === 0) return 0;
  if (n < 3) return 1;

  let prev2 = 0;
  let prev1 = 1;
  let curr = 1;

  for (let i = 3; i < n + 1; i++) {
    const summ = curr + prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
    curr = summ;
  }

  return curr;
};

// Time: O(n)
// Space: O(1)
