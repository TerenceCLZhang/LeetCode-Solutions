/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function (word1, word2) {
  if (word1.length !== word2.length) return false;

  const c1 = {};
  const c2 = {};

  for (const char of word1) c1[char] = (c1[char] || 0) + 1;
  for (const char of word2) c2[char] = (c2[char] || 0) + 1;

  const keys1 = Object.keys(c1).sort();
  const keys2 = Object.keys(c2).sort();
  const values1 = Object.values(c1).sort((a, b) => a - b);
  const values2 = Object.values(c2).sort((a, b) => a - b);

  return (
    keys1.join("") == keys2.join("") && values1.join(",") === values2.join(",")
  );
};

// Time: O(n)
// Space: O(1)
