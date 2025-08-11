class Solution {

  public int[] sortedSquares(int[] nums) {
    int n = nums.length;
    int[] squaredSorted = new int[n];
    int left = 0;
    int right = n - 1;
    int i = n - 1;

    while (left <= right) {
      int leftSquared = nums[left] * nums[left];
      int rightSquared = nums[right] * nums[right];

      if (leftSquared > rightSquared) {
        squaredSorted[i] = leftSquared;
        left++;
      } else {
        squaredSorted[i] = rightSquared;
        right--;
      }

      i--;
    }

    return squaredSorted;
  }
}
