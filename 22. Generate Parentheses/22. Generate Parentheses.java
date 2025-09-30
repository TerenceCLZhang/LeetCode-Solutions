import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<String> generateParenthesis(int n) {
    List<String> ans = new ArrayList<>();
    StringBuilder curr = new StringBuilder();

    backtrack(0, 0, n, ans, curr);
    return ans;
  }

  private void backtrack(
    int start,
    int end,
    int n,
    List<String> ans,
    StringBuilder curr
  ) {
    if (curr.length() == 2 * n) {
      ans.add(curr.toString());
      return;
    }

    if (start < n) {
      curr.append("(");
      backtrack(start + 1, end, n, ans, curr);
      curr.deleteCharAt(curr.length() - 1);
    }

    if (end < start) {
      curr.append(")");
      backtrack(start, end + 1, n, ans, curr);
      curr.deleteCharAt(curr.length() - 1);
    }
  }
}
