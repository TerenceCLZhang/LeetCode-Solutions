/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  const m = heights.length;
  const n = heights[0].length;

  // 2D arrays to check if cell has been visited
  const pSeen = Array.from({ length: m }, () => Array(n).fill(false));
  const aSeen = Array.from({ length: m }, () => Array(n).fill(false));

  const pQueue = [];
  const aQueue = [];

  for (let i = 0; i < m; i++) {
    pQueue.push([i, 0]);
    pSeen[i][0] = true;

    aQueue.push([i, n - 1]);
    aSeen[i][n - 1] = true;
  }

  for (let j = 0; j < n; j++) {
    pQueue.push([0, j]);
    pSeen[0][j] = true;

    aQueue.push([m - 1, j]);
    aSeen[m - 1][j] = true;
  }

  const bfs = (queue, seen) => {
    const directions = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ];

    while (queue.length > 0) {
      const [x, y] = queue.shift();
      for (const [dx, dy] of directions) {
        const [nx, ny] = [x + dx, y + dy];
        if (
          0 <= nx &&
          nx < m &&
          0 <= ny &&
          ny < n &&
          !seen[nx][ny] &&
          heights[x][y] <= heights[nx][ny]
        ) {
          seen[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }
  };

  bfs(pQueue, pSeen);
  bfs(aQueue, aSeen);

  const result = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pSeen[i][j] && aSeen[i][j]) {
        result.push([i, j]);
      }
    }
  }

  return result;
};
