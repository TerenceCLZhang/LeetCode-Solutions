/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function (points) {
  let time = 0;
  for (let i = 0; i < points.length - 1; i++) {
    current = points[i];
    next = points[i + 1];
    x = Math.abs(next[0] - current[0]);
    y = Math.abs(next[1] - current[1]);
    time += Math.max(x, y);
  }
  return time;
};

// Time: O(n)
// Space: O(1)
