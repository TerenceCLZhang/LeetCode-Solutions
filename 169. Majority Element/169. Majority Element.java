class Solution {

  public int majorityElement(int[] nums) {
    int currentElement = nums[0];
    int count = 0;

    for (int n : nums) {
      if (count <= 0) {
        currentElement = n;
      }

      if (currentElement == n) {
        count++;
      } else {
        count--;
      }
    }

    return currentElement;
  }
}
