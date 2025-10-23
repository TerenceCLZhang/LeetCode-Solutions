/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  const m = grid.length;
  const n = grid[0].length;

  const dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  let minutes = 0;
  let numFresh = 0;

  const queue = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        numFresh++;
      }
      if (grid[i][j] === 2) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length !== 0) {
    const currentLength = queue.length;
    for (x = 0; x < currentLength; x++) {
      const [i, j] = queue.shift();
      for (const [di, dj] of dirs) {
        const ni = i + di;
        const nj = j + dj;

        if (0 <= ni && ni < m && 0 <= nj && nj < n && grid[ni][nj] === 1) {
          grid[ni][nj] = 2;
          numFresh--;
          queue.push([ni, nj]);
        }
      }
    }

    if (queue.length !== 0) {
      minutes++;
    }
  }

  return numFresh === 0 ? minutes : -1;
};
