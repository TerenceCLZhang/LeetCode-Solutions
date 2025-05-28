/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  let stack = [];

  for (const t of tokens) {
    if (!isNaN(t)) {
      stack.push(Number(t));
    } else {
      const b = stack.pop();
      const a = stack.pop();
      switch (t) {
        case "+":
          stack.push(a + b);
          break;
        case "-":
          stack.push(a - b);
          break;
        case "*":
          stack.push(a * b);
          break;
        case "/":
          stack.push(Math.trunc(a / b));
          break;
        default:
          break;
      }
    }
  }

  return stack.pop();
};

// Time: O(n)
// Space: O(n)
