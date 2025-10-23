import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

  private static final int[][] DIRS = {
    { 1, 0 },
    { -1, 0 },
    { 0, 1 },
    { 0, -1 },
  };
  int m, n;

  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    m = heights.length;
    n = heights[0].length;

    // 2D Boolean array to check whether cell has been visisted
    boolean[][] pSeen = new boolean[m][n];
    boolean[][] aSeen = new boolean[m][n];

    Queue<int[]> pQueue = new LinkedList<>();
    Queue<int[]> aQueue = new LinkedList<>();

    for (int i = 0; i < m; i++) {
      pQueue.add(new int[] { i, 0 });
      pSeen[i][0] = true;

      aQueue.add(new int[] { i, n - 1 });
      aSeen[i][n - 1] = true;
    }
    for (int j = 0; j < n; j++) {
      pQueue.add(new int[] { 0, j });
      pSeen[0][j] = true;

      aQueue.add(new int[] { m - 1, j });
      aSeen[m - 1][j] = true;
    }

    bfs(heights, pQueue, pSeen);
    bfs(heights, aQueue, aSeen);

    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (pSeen[i][j] && aSeen[i][j]) result.add(Arrays.asList(i, j));
      }
    }
    return result;
  }

  private void bfs(int[][] heights, Queue<int[]> queue, boolean[][] seen) {
    while (!queue.isEmpty()) {
      int[] cell = queue.poll();
      int x = cell[0], y = cell[1];
      for (int[] d : DIRS) {
        int nx = x + d[0], ny = y + d[1];
        if (
          0 <= nx &&
          nx < m &&
          0 <= ny &&
          ny < n &&
          !seen[nx][ny] &&
          heights[x][y] <= heights[nx][ny]
        ) {
          seen[nx][ny] = true;
          queue.add(new int[] { nx, ny });
        }
      }
    }
  }
}
