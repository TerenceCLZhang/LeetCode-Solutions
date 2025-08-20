class Solution {

  public int longestOnes(int[] nums, int k) {
    int numFlipped = 0;
    int left = 0;
    int maxLength = 0;

    for (int curr = 0; curr < nums.length; curr++) {
      if (nums[curr] == 0) {
        numFlipped++;
      }

      while (numFlipped > k) {
        if (nums[left] == 0) {
          numFlipped--;
        }
        left += 1;
      }

      int currLength = curr - left + 1;
      maxLength = Math.max(maxLength, currLength);
    }

    return maxLength;
  }
}
