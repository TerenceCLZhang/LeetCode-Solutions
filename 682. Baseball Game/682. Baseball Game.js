/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
  const stack = [];

  for (const op of operations) {
    if (op === "+") {
      stack.push(stack.at(-1) + stack.at(-2));
    } else if (op === "D") {
      stack.push(stack.at(-1) * 2);
    } else if (op === "C") {
      stack.pop();
    } else {
      stack.push(Number(op));
    }
  }

  return stack.reduce((a, c) => a + c, 0);
};
