import java.util.HashMap;

class Solution {

  public boolean canConstruct(String ransomNote, String magazine) {
    HashMap<Character, Integer> letters = new HashMap<>();

    for (char c : magazine.toCharArray()) {
      letters.put(c, (letters.getOrDefault(c, 0)) + 1);
    }

    for (char c : ransomNote.toCharArray()) {
      if (letters.getOrDefault(c, 0) <= 0) {
        return false;
      }

      letters.put(c, letters.get(c) - 1);
    }

    return true;
  }
}
