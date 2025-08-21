class Solution {

  public int minSubArrayLen(int target, int[] nums) {
    int minLength = Integer.MAX_VALUE;
    int currSum = 0;
    int left = 0;

    for (int i = 0; i < nums.length; i++) {
      currSum += nums[i];

      while (currSum >= target) {
        minLength = Math.min(minLength, i - left + 1);
        currSum -= nums[left];
        left++;
      }
    }

    return minLength < Integer.MAX_VALUE ? minLength : 0;
  }
}
