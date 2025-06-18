/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function (s) {
  const ans = [];
  let depth = 0;

  for (const char of s) {
    if (char === "(") {
      if (depth > 0) ans.push(char);
      depth++;
    } else {
      depth--;
      if (depth > 0) ans.push(char);
    }
  }

  return ans.join("");
};

// Time: O(n)
// Space: O(n)
