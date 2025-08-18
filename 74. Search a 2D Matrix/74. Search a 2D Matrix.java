class Solution {

  public boolean searchMatrix(int[][] matrix, int target) {
    int m = matrix.length;
    int n = matrix[0].length;

    int low = 0;
    int high = m * n - 1;

    while (low <= high) {
      int mid = (low + high) / 2;
      int midI = mid / n;
      int midJ = mid % n;
      int midMatrix = matrix[midI][midJ];

      if (midMatrix == target) {
        return true;
      } else if (midMatrix > target) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return false;
  }
}
