import java.util.ArrayList;
import java.util.List;

class Solution {

  public String convert(String s, int numRows) {
    if (numRows == 1) {
      return s;
    }

    List<StringBuilder> rows = new ArrayList<>();
    for (int i = 0; i < numRows; i++) {
      rows.add(new StringBuilder());
    }

    int pos = 0;
    int dPos = 1;

    for (char c : s.toCharArray()) {
      rows.get(pos).append(c);

      if (pos == numRows - 1) {
        dPos = -1;
      } else if (pos == 0) {
        dPos = 1;
      }

      pos += dPos;
    }

    StringBuilder zigZag = new StringBuilder();
    for (StringBuilder row : rows) {
      zigZag.append(row);
    }

    return zigZag.toString();
  }
}
