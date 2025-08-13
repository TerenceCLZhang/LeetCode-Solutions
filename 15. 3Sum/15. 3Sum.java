import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    int n = nums.length;
    List<List<Integer>> sums = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      if (nums[i] > 0) {
        break;
      }

      if (i != 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int left = i + 1;
      int right = n - 1;

      while (left < right) {
        int summ = nums[i] + nums[left] + nums[right];
        if (summ == 0) {
          sums.add(Arrays.asList(nums[i], nums[left], nums[right]));

          left++;
          right--;

          while (left < right && nums[left] == nums[left - 1]) {
            left++;
          }

          while (left < right && nums[right] == nums[right + 1]) {
            right--;
          }
        } else if (summ > 0) {
          right--;
        } else {
          left++;
        }
      }
    }

    return sums;
  }
}
