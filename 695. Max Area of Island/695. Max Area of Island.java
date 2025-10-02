class Solution {

  int m, n;

  public int maxAreaOfIsland(int[][] grid) {
    m = grid.length;
    n = grid[0].length;

    int maxArea = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          int currentArea = dfs(i, j, grid);
          maxArea = Math.max(maxArea, currentArea);
        }
      }
    }

    return maxArea;
  }

  private int dfs(int i, int j, int[][] grid) {
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1) {
      return 0;
    }

    grid[i][j] = 0;

    return (
      1 +
      dfs(i + 1, j, grid) +
      dfs(i - 1, j, grid) +
      dfs(i, j + 1, grid) +
      dfs(i, j - 1, grid)
    );
  }
}
