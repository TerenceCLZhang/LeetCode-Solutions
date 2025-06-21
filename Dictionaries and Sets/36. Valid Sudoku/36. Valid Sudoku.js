/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  for (let i = 0; i < 9; i++) {
    set = new Set();
    for (let j = 0; j < 9; j++) {
      if (set.has(board[i][j])) return false;
      else if (board[i][j] !== ".") set.add(board[i][j]);
    }
  }

  for (let i = 0; i < 9; i++) {
    set = new Set();
    for (let j = 0; j < 9; j++) {
      if (set.has(board[j][i])) return false;
      else if (board[j][i] !== ".") set.add(board[j][i]);
    }
  }

  const starts = [
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

  for (const [i, j] of starts) {
    set = new Set();
    for (let row = i; row < i + 3; row++) {
      for (let col = j; col < j + 3; col++) {
        if (set.has(board[row][col])) return false;
        else if (board[row][col] !== ".") set.add(board[row][col]);
      }
    }
  }

  return true;
};

// Time: O(1)
// Space: O(1)
