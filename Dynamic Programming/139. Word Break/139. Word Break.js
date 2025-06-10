/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  wordDict = new Set(wordDict);
  const dp = new Array(s.length).fill(false);

  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordDict.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp.at(-1);
};

// Time: O(n^2)
// Space: O(n + m)
