/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function (s) {
  let stack = [];
  for (const char of s) {
    if (stack && char === "*") stack.pop();
    else stack.push(char);
  }
  return stack.join("");
};

// Time: O(n)
// Space: O(n)
