class Solution {

  int m, n;

  public int numIslands(char[][] grid) {
    m = grid.length;
    n = grid[0].length;

    int numIslands = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '1') {
          dfs(i, j, grid);
          numIslands++;
        }
      }
    }

    return numIslands;
  }

  private void dfs(int i, int j, char[][] grid) {
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {
      return;
    }

    grid[i][j] = '0';

    dfs(i + 1, j, grid);
    dfs(i - 1, j, grid);
    dfs(i, j + 1, grid);
    dfs(i, j - 1, grid);
  }
}
