import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<List<Integer>> permute(int[] nums) {
    int n = nums.length;
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> curr = new ArrayList<>();
    boolean[] used = new boolean[n];

    backtrack(nums, n, ans, curr, used);
    return ans;
  }

  private void backtrack(
    int[] nums,
    int n,
    List<List<Integer>> ans,
    List<Integer> curr,
    boolean[] used
  ) {
    if (curr.size() == n) {
      ans.add(new ArrayList<>(curr));
      return;
    }

    for (int i = 0; i < n; i++) {
      if (!used[i]) {
        curr.add(nums[i]);
        used[i] = true;
        backtrack(nums, n, ans, curr, used);
        curr.remove(curr.size() - 1);
        used[i] = false;
      }
    }
  }
}
