/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  if (n < 2) return n;

  let curr = 0;
  let prev2 = 0;
  let prev1 = 1;

  for (let i = 2; i < n + 1; i++) {
    curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }

  return curr;
};

// Time: O(n)
// Space: O(1)
