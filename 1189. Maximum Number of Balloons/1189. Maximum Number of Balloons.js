/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function (text) {
  const letters = { b: 0, a: 0, l: 0, o: 0, n: 0 };

  for (const c of text) {
    if (c in letters) {
      letters[c]++;
    }
  }

  return Math.min(
    letters["b"],
    letters["a"],
    Math.floor(letters["l"] / 2),
    Math.floor(letters["o"] / 2),
    letters["n"]
  );
};
