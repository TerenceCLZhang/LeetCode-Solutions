import java.util.Arrays;

class Solution {

  public boolean checkInclusion(String s1, String s2) {
    int s1Len = s1.length();
    int s2Len = s2.length();

    if (s1Len > s2Len) {
      return false;
    }

    int[] s1Count = new int[26];
    int[] s2Count = new int[26];

    for (int i = 0; i < s1Len; i++) {
      s1Count[s1.charAt(i) - 'a']++;
      s2Count[s2.charAt(i) - 'a']++;
    }

    if (Arrays.equals(s1Count, s2Count)) {
      return true;
    }

    for (int i = s1Len; i < s2Len; i++) {
      s2Count[s2.charAt(i) - 'a']++;
      s2Count[s2.charAt(i - s1Len) - 'a']--;

      if (Arrays.equals(s1Count, s2Count)) {
        return true;
      }
    }

    return false;
  }
}
