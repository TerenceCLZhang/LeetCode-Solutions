/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  anagrams = {};
  for (const s of strs) {
    alphabet = new Array(26).fill(0);
    for (const char of s) {
      alphabet[char.charCodeAt(0) - "a".charCodeAt(0)]++;
    }
    alphabet = alphabet.join(",");
    if (anagrams[alphabet]) anagrams[alphabet].push(s);
    else anagrams[alphabet] = [s];
  }
  return Object.values(anagrams);
};

// Time: O(n * m)
// Space: O(n)
// Where n is the number of strings and m is the longest string
