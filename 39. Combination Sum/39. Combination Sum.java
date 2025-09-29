import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> curr = new ArrayList<>();

    backtrack(0, 0, candidates, target, ans, curr);
    return ans;
  }

  private void backtrack(
    int start,
    int currSum,
    int[] candidates,
    int target,
    List<List<Integer>> ans,
    List<Integer> curr
  ) {
    if (currSum == target) {
      ans.add(new ArrayList<>(curr));
      return;
    }

    if (currSum > target) {
      return;
    }

    for (int i = start; i < candidates.length; i++) {
      curr.add(candidates[i]);
      backtrack(i, currSum + candidates[i], candidates, target, ans, curr);
      curr.remove(curr.size() - 1);
    }
  }
}
