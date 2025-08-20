/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const seen = new Set();
  let left = 0;
  let maxLength = 0;

  for (let i = 0; i < s.length; i++) {
    while (seen.has(s[i])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[i]);

    const currLength = i - left + 1;
    maxLength = Math.max(maxLength, currLength);
  }

  return maxLength;
};
