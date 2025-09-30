/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const ans = [];
  const curr = [];

  const backtrack = (start, end) => {
    if (curr.length === 2 * n) {
      ans.push(curr.join(""));
      return;
    }

    if (start < n) {
      curr.push("(");
      backtrack(start + 1, end);
      curr.pop();
    }

    if (end < start) {
      curr.push(")");
      backtrack(start, end + 1);
      curr.pop();
    }
  };

  backtrack(0, 0);
  return ans;
};
