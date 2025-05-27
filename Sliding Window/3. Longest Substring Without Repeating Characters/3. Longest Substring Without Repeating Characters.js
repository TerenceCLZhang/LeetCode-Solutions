/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let l = 0;
  let sett = new Set();
  let longest = 0;

  for (let r = 0; r < s.length; r++) {
    while (sett.has(s[r])) {
      sett.delete(s[l]);
      l++;
    }

    sett.add(s[r]);
    longest = Math.max(longest, sett.size);
  }

  return longest;
};

// Time: O(n)
// Space: O(n)
