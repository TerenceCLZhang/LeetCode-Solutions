/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  minLength = Infinity;
  for (const s of strs) {
    if (s.length < minLength) {
      minLength = s.length;
    }
  }

  for (let i = 0; i < minLength; i++) {
    for (const s of strs) {
      if (strs[0][i] !== s[i]) {
        return s.slice(0, i);
      }
    }
  }

  return strs[0].slice(0, minLength);
};
