/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  const gcd = (a, b) => {
    while (b) {
      [a, b] = [b, a % b];
    }
    return a;
  };

  if (str1 + str2 !== str2 + str1) return "";
  const size = gcd(str1.length, str2.length);
  return str1.slice(0, size);
};

// Time: O(n + m)
// Space: O(n + m)
