/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let min_length = Infinity;
  for (let s of strs) min_length = Math.min(min_length, s.length);

  for (let i = 0; i < min_length; i++) {
    const current_char = strs[0][i];
    for (let s of strs) {
      if (s[i] !== current_char) return s.slice(0, i);
    }
  }

  return strs[0].slice(0, min_length);
};

// Time: O(n * m)
// Space: O(1)
