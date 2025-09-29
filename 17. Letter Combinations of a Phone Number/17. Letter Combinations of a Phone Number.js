/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits === "") {
    return [];
  }

  const digitsMap = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };

  const n = digits.length;
  const ans = [];
  const curr = [];

  const backtrack = (i) => {
    if (curr.length === n) {
      ans.push(curr.join(""));
      return;
    }

    for (const c of digitsMap[digits[i]]) {
      curr.push(c);
      backtrack(i + 1);
      curr.pop();
    }
  };

  backtrack(0);
  return ans;
};
