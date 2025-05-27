/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const compliment = { ")": "(", "}": "{", "]": "[" };
  let stack = [];

  for (let char of s) {
    if (!(char in compliment)) stack.push(char);
    else {
      if (stack.length === 0 || stack[stack.length - 1] !== compliment[char]) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
};

// Time: O(n)
// Space: O(n)
