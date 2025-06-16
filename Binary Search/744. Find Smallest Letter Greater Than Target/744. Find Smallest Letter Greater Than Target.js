/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function (letters, target) {
  let l = 0;
  let r = letters.length;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    if (letters[m] > target) r = m - 1;
    else l = m + 1;
  }

  if (l < letters.length) return letters[l];
  return letters[0];
};

// Time: O(log n)
// Space: O(1)
