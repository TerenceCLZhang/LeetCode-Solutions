class Solution {

  int m, n, w;
  boolean[][] seen;

  public boolean exist(char[][] board, String word) {
    m = board.length;
    n = board[0].length;
    w = word.length();
    seen = new boolean[m][n];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (backtrack(i, j, 0, board, word)) {
          return true;
        }
      }
    }

    return false;
  }

  private boolean backtrack(
    int i,
    int j,
    int index,
    char[][] board,
    String word
  ) {
    if (index == w) {
      return true;
    }

    if (
      i < 0 ||
      i >= m ||
      j < 0 ||
      j >= n ||
      board[i][j] != word.charAt(index) ||
      seen[i][j]
    ) {
      return false;
    }

    seen[i][j] = true;

    boolean found =
      backtrack(i + 1, j, index + 1, board, word) ||
      backtrack(i - 1, j, index + 1, board, word) ||
      backtrack(i, j + 1, index + 1, board, word) ||
      backtrack(i, j - 1, index + 1, board, word);

    seen[i][j] = false;
    return found;
  }
}
