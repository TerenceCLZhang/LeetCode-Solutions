/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function (s) {
  const vowels = new Array(26).fill(0);
  const consonants = new Array(26).fill(0);

  for (let char of s) {
    const i = char.charCodeAt(0) - "a".charCodeAt(0);
    if ("aeiou".includes(char)) vowels[i]++;
    else consonants[i]++;
  }

  return Math.max(...vowels) + Math.max(...consonants);
};

// Time: O(n)
// Space: O(1)
