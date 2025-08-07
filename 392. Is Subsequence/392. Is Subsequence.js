/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  if (s === "") {
    return true;
  }

  const n = s.length;
  const m = t.length;

  if (n > m) {
    return false;
  }

  let i = 0;
  for (let j = 0; j < m; j++) {
    if (s[i] == t[j]) {
      i++;
    }

    if (i == n) {
      return true;
    }
  }

  return false;
};
