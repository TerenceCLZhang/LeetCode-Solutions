/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function (arr) {
  arr.sort((a, b) => a - b);
  let min_abs_diff = Infinity;
  let ans = [];

  for (let i = 1; i < arr.length; i++) {
    const diff = arr[i] - arr[i - 1];
    if (diff < min_abs_diff) {
      min_abs_diff = diff;
      ans = [[arr[i - 1], arr[i]]];
    } else if (diff === min_abs_diff) {
      ans.push([arr[i - 1], arr[i]]);
    }
  }

  return ans;
};

// Time: O(n log n)
// Space: O(1)
