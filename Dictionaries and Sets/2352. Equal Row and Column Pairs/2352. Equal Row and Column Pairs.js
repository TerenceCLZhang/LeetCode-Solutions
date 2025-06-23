/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function (grid) {
  const rows = {};

  for (const row of grid) {
    const r = row.join(",");
    rows[r] = (rows[r] || 0) + 1;
  }

  let pairs = 0;
  for (let j = 0; j < grid.length; j++) {
    let key = [];
    for (let i = 0; i < grid.length; i++) {
      key.push(grid[i][j]);
    }
    key = key.join(",");
    if (key in rows) {
      pairs += rows[key];
    }
  }

  return pairs;
};

// Time: O(n^2)
// Space: O(1)
