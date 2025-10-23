import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

  public int orangesRotting(int[][] grid) {
    int m = grid.length;
    int n = grid[0].length;

    int[][] dirs = new int[][] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    int minutes = 0;
    int numFresh = 0;

    Queue<int[]> queue = new LinkedList<>();

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          numFresh++;
        }
        if (grid[i][j] == 2) {
          queue.add(new int[] { i, j });
        }
      }
    }

    while (!queue.isEmpty()) {
      int currentLength = queue.size();

      for (int x = 0; x < currentLength; x++) {
        int[] pair = queue.poll();

        for (int[] dir : dirs) {
          int ni = pair[0] + dir[0];
          int nj = pair[1] + dir[1];

          if (0 <= ni && ni < m && 0 <= nj && nj < n && grid[ni][nj] == 1) {
            grid[ni][nj] = 2;
            numFresh--;
            queue.add(new int[] { ni, nj });
          }
        }
      }

      if (!queue.isEmpty()) {
        minutes++;
      }
    }

    return numFresh == 0 ? minutes : -1;
  }
}
