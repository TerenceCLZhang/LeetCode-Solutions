/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  let ans = [],
    curr = [];

  const backtrack = (open, close) => {
    if (open === close && close === n) {
      ans.push(curr.join(""));
      return;
    }

    if (open < n) {
      curr.push("(");
      backtrack(open + 1, close);
      curr.pop();
    }

    if (open > close) {
      curr.push(")");
      backtrack(open, close + 1);
      curr.pop();
    }
  };

  backtrack(0, 0);
  return ans;
};

// Time: O(4 ^ n / sqrt(n))
// Space: O(n)
