import java.util.HashSet;
import java.util.Set;

class Solution {

  public int lengthOfLongestSubstring(String s) {
    Set<Character> seen = new HashSet<>();
    int left = 0;
    int maxLength = 0;

    for (int i = 0; i < s.length(); i++) {
      while (seen.contains(s.charAt(i))) {
        seen.remove(s.charAt(left));
        left++;
      }

      seen.add(s.charAt(i));

      int currLength = i - left + 1;
      maxLength = Math.max(maxLength, currLength);
    }

    return maxLength;
  }
}
