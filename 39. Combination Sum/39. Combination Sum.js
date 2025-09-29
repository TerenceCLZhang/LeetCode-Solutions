/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  n = candidates.length;
  const ans = [];
  const curr = [];

  const backtrack = (start, currSum) => {
    if (currSum === target) {
      ans.push([...curr]);
      return;
    }

    if (currSum > target) {
      return;
    }

    for (let i = start; i < n; i++) {
      curr.push(candidates[i]);
      backtrack(i, currSum + candidates[i]);
      curr.pop();
    }
  };

  backtrack(0, 0);
  return ans;
};
