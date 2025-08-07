class Solution {

  public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
      return false;
    }

    int[] sCounter = new int[26];
    int[] tCounter = new int[26];

    for (int i = 0; i < s.length(); i++) {
      sCounter[s.charAt(i) - 'a']++;
      tCounter[t.charAt(i) - 'a']++;
    }

    return Arrays.equals(sCounter, tCounter);
  }
}
