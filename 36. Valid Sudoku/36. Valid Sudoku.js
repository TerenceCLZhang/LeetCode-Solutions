/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  for (let i = 0; i < 9; i++) {
    const seen = new Set();
    for (let j = 0; j < 9; j++) {
      const cell = board[i][j];
      if (cell !== ".") {
        if (seen.has(cell)) {
          return false;
        }
        seen.add(cell);
      }
    }
  }

  for (let j = 0; j < 9; j++) {
    const seen = new Set();
    for (let i = 0; i < 9; i++) {
      const cell = board[i][j];
      if (cell !== ".") {
        if (seen.has(cell)) {
          return false;
        }
        seen.add(cell);
      }
    }
  }

  const gridStarts = [
    [0, 0],
    [0, 3],
    [0, 6],
    [3, 0],
    [3, 3],
    [3, 6],
    [6, 0],
    [6, 3],
    [6, 6],
  ];

  for (const [startX, startY] of gridStarts) {
    const seen = new Set();
    for (let i = startX; i < startX + 3; i++) {
      for (let j = startY; j < startY + 3; j++) {
        const cell = board[i][j];
        if (cell !== ".") {
          if (seen.has(cell)) {
            return false;
          }
          seen.add(cell);
        }
      }
    }
  }

  return true;
};
