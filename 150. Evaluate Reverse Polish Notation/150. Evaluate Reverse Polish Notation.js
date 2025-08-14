/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const stack = [];

  for (const t of tokens) {
    if ("+-*/".includes(t)) {
      const val2 = stack.pop();
      const val1 = stack.pop();

      switch (t) {
        case "+":
          stack.push(val1 + val2);
          break;
        case "-":
          stack.push(val1 - val2);
          break;
        case "*":
          stack.push(val1 * val2);
          break;
        case "/":
          stack.push(Math.trunc(val1 / val2));
          break;
        default:
          break;
      }
    } else {
      stack.push(Number(t));
    }
  }

  return stack.pop();
};
