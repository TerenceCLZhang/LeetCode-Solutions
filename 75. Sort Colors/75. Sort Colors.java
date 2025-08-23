class Solution {

  public void sortColors(int[] nums) {
    int low = 0;
    int curr = 0;
    int high = nums.length - 1;

    while (curr <= high) {
      if (nums[curr] == 0) {
        swapElements(nums, low, curr);
        low++;
        curr++;
      } else if (nums[curr] == 1) {
        curr++;
      } else {
        swapElements(nums, curr, high);
        high--;
      }
    }
  }

  private void swapElements(int[] nums, int a, int b) {
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }
}
