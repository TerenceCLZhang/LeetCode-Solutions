import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

class Solution {

  public List<String> summaryRanges(int[] nums) {
    if (nums.length == 0) {
      return Collections.emptyList();
    }

    List<String> summaryRanges = new ArrayList<>();
    int start = 0;

    for (int i = 1; i < nums.length + 1; i++) {
      if (i == nums.length || nums[i] != nums[i - 1] + 1) {
        if (start == i - 1) {
          summaryRanges.add(String.format("%d", nums[start]));
        } else {
          summaryRanges.add(String.format("%d->%d", nums[start], nums[i - 1]));
        }

        start = i;
      }
    }

    return summaryRanges;
  }
}
