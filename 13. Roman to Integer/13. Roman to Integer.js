/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const symbolMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  const n = s.length;
  let total = 0;
  let i = 0;

  while (i < n) {
    if (i < n - 1 && symbolMap[s[i]] < symbolMap[s[i + 1]]) {
      total += symbolMap[s[i + 1]] - symbolMap[s[i]];
      i += 2;
    } else {
      total += symbolMap[s[i]];
      i++;
    }
  }

  return total;
};
