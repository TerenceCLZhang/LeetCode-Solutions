class Solution {

  public int findClosestNumber(int[] nums) {
    int closest = nums[0];

    for (int num : nums) {
      if (Math.abs(num) < Math.abs(closest)) {
        closest = num;
      }
    }

    if (closest < 0 && contains(nums, Math.abs(closest))) {
      closest *= -1;
    }

    return closest;
  }

  private boolean contains(int[] nums, int closest) {
    for (int i = 0; i < nums.length; i++) {
      if (closest == nums[i]) {
        return true;
      }
    }
    return false;
  }
}
