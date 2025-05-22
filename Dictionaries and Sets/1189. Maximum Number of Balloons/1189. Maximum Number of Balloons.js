/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function (text) {
  const balloon = { b: 0, a: 0, l: 0, o: 0, n: 0 };
  for (let c of text) {
    if (c in balloon) balloon[c]++;
  }
  return Math.min(
    balloon["b"],
    balloon["a"],
    Math.floor(balloon["l"] / 2),
    Math.floor(balloon["o"] / 2),
    balloon["n"]
  );
};

// Time: O(n)
// Space: O(1)
