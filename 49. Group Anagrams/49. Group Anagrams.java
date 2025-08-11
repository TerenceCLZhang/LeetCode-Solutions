import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

  public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> anagrams = new HashMap<>();

    for (String s : strs) {
      int[] alphabet = new int[26];
      for (char c : s.toCharArray()) {
        alphabet[c - 'a']++;
      }
      StringBuilder key = new StringBuilder();
      for (int num : alphabet) {
        key.append(num).append(',');
      }
      String keyString = key.toString();
      anagrams.computeIfAbsent(keyString, k -> new ArrayList<>()).add(s);
    }

    return new ArrayList<>(anagrams.values());
  }
}
