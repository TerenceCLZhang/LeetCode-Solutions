/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  const l1 = word1.length;
  const l2 = word2.length;
  const maxLength = Math.max(l1, l2);
  const merged = [];

  for (let i = 0; i < maxLength; i++) {
    if (i < l1) {
      merged.push(word1[i]);
    }

    if (i < l2) {
      merged.push(word2[i]);
    }
  }

  return merged.join("");
};
