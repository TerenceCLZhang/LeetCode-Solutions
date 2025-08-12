import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<Integer> spiralOrder(int[][] matrix) {
    int m = matrix.length, n = matrix[0].length;
    List<Integer> spiral = new ArrayList<>();

    int top = 0, bottom = m - 1;
    int left = 0, right = n - 1;

    while (left <= right && top <= bottom) {
      for (int j = left; j <= right; j++) {
        spiral.add(matrix[top][j]);
      }
      top++;

      for (int i = top; i <= bottom; i++) {
        spiral.add(matrix[i][right]);
      }
      right--;

      if (top <= bottom) {
        for (int j = right; j >= left; j--) {
          spiral.add(matrix[bottom][j]);
        }
        bottom--;
      }

      if (left <= right) {
        for (int i = bottom; i >= top; i--) {
          spiral.add(matrix[i][left]);
        }
        left++;
      }
    }

    return spiral;
  }
}
