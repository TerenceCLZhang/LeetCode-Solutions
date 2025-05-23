/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    if (!/^[a-z0-9]$/i.test(s[l])) {
      l++;
      continue;
    }

    if (!/^[a-z0-9]$/i.test(s[r])) {
      r--;
      continue;
    }

    if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    l++;
    r--;
  }
  return true;
};

// Time: O(n)
// Space: O(1)
