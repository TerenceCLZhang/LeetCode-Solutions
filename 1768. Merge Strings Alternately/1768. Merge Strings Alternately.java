class Solution {

  public String mergeAlternately(String word1, String word2) {
    int l1 = word1.length();
    int l2 = word2.length();
    int maxLength = Math.max(l1, l2);
    StringBuilder merged = new StringBuilder();

    for (int i = 0; i < maxLength; i++) {
      if (i < l1) {
        merged.append(word1.charAt(i));
      }

      if (i < l2) {
        merged.append(word2.charAt(i));
      }
    }

    return merged.toString();
  }
}
