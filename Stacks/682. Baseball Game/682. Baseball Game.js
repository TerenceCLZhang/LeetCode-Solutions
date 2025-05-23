/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
  let stack = [];
  for (let op of operations) {
    if (op === "+")
      stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
    else if (op === "D") stack.push(stack[stack.length - 1] * 2);
    else if (op === "C") stack.pop();
    else stack.push(Number(op));
  }

  return stack.reduce((a, c) => a + c, 0);
};

// Time: O(n)
// Space: O(n)
