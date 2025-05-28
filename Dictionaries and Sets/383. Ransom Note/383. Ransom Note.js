/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  let letters = {};
  for (const m of magazine) {
    if (m in letters) letters[m]++;
    else letters[m] = 1;
  }

  for (const c of ransomNote) {
    if (!(c in letters)) return false;
    if (letters[c] === 1) delete letters[c];
    else letters[c]--;
  }

  return true;
};

// Time: O(n + m)
// Space: O(n)
