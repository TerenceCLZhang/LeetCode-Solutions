/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const merged = [];

  for (const interval of intervals) {
    n = merged.length;
    if (n === 0 || merged[n - 1][1] < interval[0]) {
      merged.push(interval);
    } else {
      merged[n - 1][1] = Math.max(merged[n - 1][1], interval[1]);
    }
  }

  return merged;
};
