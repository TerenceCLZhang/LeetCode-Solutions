/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  if (n < 2) return n;

  let prev = 0;
  let curr = 1;

  for (let i = 2; i <= n; i++) {
    [prev, curr] = [curr, prev + curr];
  }

  return curr;
};

// Time: O(n)
// Space: O(1)
