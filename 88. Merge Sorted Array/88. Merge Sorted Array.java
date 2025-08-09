class Solution {

  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int end1 = m - 1;
    int end2 = n - 1;

    for (int i = m + n - 1; i > -1; i--) {
      if (end2 < 0) {
        break;
      } else if (end1 >= 0 && nums1[end1] > nums2[end2]) {
        nums1[i] = nums1[end1];
        end1--;
      } else {
        nums1[i] = nums2[end2];
        end2--;
      }
    }
  }
}
