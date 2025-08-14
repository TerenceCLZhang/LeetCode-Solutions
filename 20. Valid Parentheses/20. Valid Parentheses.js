/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const parentheses = new Map([
    [")", "("],
    ["]", "["],
    ["}", "{"],
  ]);
  const stack = [];

  for (const char of s) {
    if (parentheses.has(char)) {
      if (!stack) {
        return false;
      }

      const popped = stack.pop();
      if (popped !== parentheses.get(char)) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
};
