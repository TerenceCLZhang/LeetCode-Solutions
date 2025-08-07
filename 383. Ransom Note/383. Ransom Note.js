/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  const letters = {};

  for (const c of magazine) {
    letters[c] = (letters[c] || 0) + 1;
  }

  for (const c of ransomNote) {
    if (!letters[c] || letters[c] <= 0) {
      return false;
    }

    letters[c]--;
  }

  return true;
};
