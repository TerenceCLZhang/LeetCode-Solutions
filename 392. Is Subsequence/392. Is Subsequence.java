class Solution {

  public boolean isSubsequence(String s, String t) {
    if (s.isEmpty()) {
      return true;
    }

    int n = s.length();
    int m = t.length();

    if (n > m) {
      return false;
    }

    int i = 0;
    for (int j = 0; j < m; j++) {
      if (s.charAt(i) == t.charAt(j)) {
        i++;
      }

      if (i == n) {
        return true;
      }
    }

    return false;
  }
}
