/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function (words, x) {
  let ans = [];
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes(x)) ans.push(i);
  }
  return ans;
};

// Time: O(n * m)
// Space: O(1)
