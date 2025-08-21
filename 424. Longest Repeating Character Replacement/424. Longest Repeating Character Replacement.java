class Solution {

  public int characterReplacement(String s, int k) {
    int[] alphabet = new int[26];
    int maxLength = 0;
    int maxCount = 0;
    int left = 0;

    for (int i = 0; i < s.length(); i++) {
      int alphabetIndex = s.charAt(i) - 'A';
      alphabet[alphabetIndex]++;
      maxCount = Math.max(maxCount, alphabet[alphabetIndex]);

      while (i - left + 1 - maxCount > k) {
        alphabet[s.charAt(left) - 'A']--;
        left++;
      }

      maxLength = Math.max(maxLength, i - left + 1);
    }

    return maxLength;
  }
}
