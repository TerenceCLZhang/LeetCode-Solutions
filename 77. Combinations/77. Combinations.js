/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  const ans = [];
  const curr = [];

  const backtrack = (start) => {
    if (curr.length == k) {
      ans.push([...curr]);
      return;
    }

    for (let i = start; i < n + 1; i++) {
      curr.push(i);
      backtrack(i + 1);
      curr.pop();
    }
  };

  backtrack(1);
  return ans;
};
