/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const anagrams = new Map();

  for (const s of strs) {
    const alphabet = new Array(26).fill(0);
    for (const c of s) {
      alphabet[c.charCodeAt(0) - "a".charCodeAt(0)]++;
    }
    const key = alphabet.join(",");
    if (!anagrams.get(key)) {
      anagrams.set(key, []);
    }
    anagrams.get(key).push(s);
  }

  return Array.from(anagrams.values());
};
