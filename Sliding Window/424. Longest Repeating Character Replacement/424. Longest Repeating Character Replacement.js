/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  const characters = new Array(26).fill(0);
  let longest = 0;
  let l = 0;

  for (let r = 0; r < s.length; r++) {
    characters[s[r].charCodeAt(0) - "A".charCodeAt(0)]++;

    if (r - l + 1 - Math.max(...characters) > k) {
      characters[s[l].charCodeAt(0) - "A".charCodeAt(0)]--;
      l++;
    }

    longest = Math.max(longest, r - l + 1);
  }

  return longest;
};

// Time: O(n)
// Space: O(1)
