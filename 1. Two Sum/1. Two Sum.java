import java.util.HashMap;
import java.util.Map;

class Solution {

  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> complements = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int needed = target - nums[i];
      if (complements.containsKey(needed)) {
        return new int[] { complements.get(needed), i };
      }
      complements.put(nums[i], i);
    }

    throw new Error("No solution");
  }
}
