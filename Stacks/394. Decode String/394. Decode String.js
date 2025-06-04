/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  let stack = [];

  for (const char of s) {
    if (char !== "]") stack.push(char);
    else {
      let currString = "";
      while (stack.at(-1) !== "[") {
        currString = stack.pop() + currString;
      }
      stack.pop();

      let num = "";
      while (stack && !isNaN(stack.at(-1))) {
        num = stack.pop() + num;
      }

      stack.push(currString.repeat(Number(num)));
    }
  }

  return stack.join("");
};

// Time: O(L)
// Space: O(L)
// Where L is the length of the decoded string
