/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
  const vowels = "aeiou";
  let num_vowels = 0;

  for (let i = 0; i < k; i++) {
    if (vowels.includes(char)) num_vowels++;
  }

  let max_vowels = num_vowels;

  for (let i = k; i < s.length; i++) {
    if (vowels.includes(s[i - k])) num_vowels--;
    if (vowels.includes(s[i])) num_vowels++;

    max_vowels = Math.max(max_vowels, num_vowels);
  }

  return max_vowels;
};

// Time: O(n)
// Space: O(1)
