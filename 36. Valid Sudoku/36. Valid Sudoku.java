import java.util.HashSet;
import java.util.Set;

class Solution {

  public boolean isValidSudoku(char[][] board) {
    for (int i = 0; i < 9; i++) {
      Set<Character> seen = new HashSet<>();
      for (int j = 0; j < 9; j++) {
        char cell = board[i][j];
        if (cell != '.') {
          if (seen.contains(cell)) {
            return false;
          }
          seen.add(cell);
        }
      }
    }

    for (int j = 0; j < 9; j++) {
      Set<Character> seen = new HashSet<>();
      for (int i = 0; i < 9; i++) {
        char cell = board[i][j];
        if (cell != '.') {
          if (seen.contains(cell)) {
            return false;
          }
          seen.add(cell);
        }
      }
    }

    int[][] gridStarts = {
      { 0, 0 },
      { 0, 3 },
      { 0, 6 },
      { 3, 0 },
      { 3, 3 },
      { 3, 6 },
      { 6, 0 },
      { 6, 3 },
      { 6, 6 },
    };

    for (int[] gridStart : gridStarts) {
      int startX = gridStart[0];
      int startY = gridStart[1];
      Set<Character> seen = new HashSet<>();
      for (int i = startX; i < startX + 3; i++) {
        for (int j = startY; j < startY + 3; j++) {
          char cell = board[i][j];
          if (cell != '.') {
            if (seen.contains(cell)) {
              return false;
            }
            seen.add(cell);
          }
        }
      }
    }

    return true;
  }
}
