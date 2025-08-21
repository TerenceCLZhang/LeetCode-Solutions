/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  const alphabet = new Array(26).fill(0);
  let maxLength = 0;
  let maxCount = 0;
  let left = 0;

  for (let i = 0; i < s.length; i++) {
    const alphabetIndex = s.charCodeAt(i) - "A".charCodeAt(0);
    alphabet[alphabetIndex]++;
    maxCount = Math.max(maxCount, alphabet[alphabetIndex]);

    while (i - left + 1 - Math.max(...alphabet) > k) {
      alphabet[s.charCodeAt(left) - "A".charCodeAt(0)]--;
      left++;
    }

    maxLength = Math.max(maxLength, i - left + 1);
  }

  return maxLength;
};
