/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const m = matrix.length,
    n = matrix[0].length;
  const spiral = [];

  let top = 0,
    bottom = m - 1;
  let left = 0,
    right = n - 1;

  while (left <= right && top <= bottom) {
    for (let j = left; j <= right; j++) {
      spiral.push(matrix[top][j]);
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      spiral.push(matrix[i][right]);
    }
    right--;

    if (top <= bottom) {
      for (let j = right; j >= left; j--) {
        spiral.push(matrix[bottom][j]);
      }
      bottom--;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        spiral.push(matrix[i][left]);
      }
      left++;
    }
  }

  return spiral;
};
