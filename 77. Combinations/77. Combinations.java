import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<List<Integer>> combine(int n, int k) {
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> curr = new ArrayList<>();

    backtrack(1, n, k, ans, curr);
    return ans;
  }

  private void backtrack(
    int start,
    int n,
    int k,
    List<List<Integer>> ans,
    List<Integer> curr
  ) {
    if (curr.size() == k) {
      ans.add(new ArrayList<>(curr));
      return;
    }

    for (int i = start; i < n + 1; i++) {
      curr.add(i);
      backtrack(i + 1, n, k, ans, curr);
      curr.remove(curr.size() - 1);
    }
  }
}
