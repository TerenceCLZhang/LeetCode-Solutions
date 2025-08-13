import java.util.HashSet;
import java.util.Set;

class Solution {

  public int longestConsecutive(int[] nums) {
    Set<Integer> unique = new HashSet<>();
    for (int n : nums) {
      unique.add(n);
    }

    int largest = 0;

    for (int n : unique) {
      if (!unique.contains(n - 1)) {
        int current = 0;
        while (unique.contains(n)) {
          current++;
          n++;
        }
        largest = Math.max(largest, current);
      }
    }

    return largest;
  }
}
