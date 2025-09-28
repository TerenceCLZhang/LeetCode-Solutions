import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<List<Integer>> subsets(int[] nums) {
    int n = nums.length;
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> curr = new ArrayList<>();

    backtrack(nums, 0, n, curr, ans);
    return ans;
  }

  private void backtrack(
    int[] nums,
    int i,
    int n,
    List<Integer> curr,
    List<List<Integer>> ans
  ) {
    if (i == n) {
      ans.add(new ArrayList<>(curr));
      return;
    }

    backtrack(nums, i + 1, n, curr, ans);

    curr.add(nums[i]);
    backtrack(nums, i + 1, n, curr, ans);
    curr.remove(curr.size() - 1);
  }
}
