import java.util.Arrays;

class Solution {

  public int threeSumClosest(int[] nums, int target) {
    Arrays.sort(nums);
    int n = nums.length;
    int closest = nums[0] + nums[1] + nums[2];

    for (int i = 0; i < n - 2; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int left = i + 1;
      int right = n - 1;

      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];

        if (sum == target) {
          return sum;
        }

        if (Math.abs(target - sum) < Math.abs(target - closest)) {
          closest = sum;
        }

        if (sum < target) {
          left++;
        } else {
          right--;
        }
      }
    }

    return closest;
  }
}
