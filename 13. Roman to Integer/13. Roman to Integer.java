import java.util.HashMap;
import java.util.Map;

class Solution {

  public int romanToInt(String s) {
    Map<Character, Integer> symbolMap = new HashMap<>();
    symbolMap.put('I', 1);
    symbolMap.put('V', 5);
    symbolMap.put('X', 10);
    symbolMap.put('L', 50);
    symbolMap.put('C', 100);
    symbolMap.put('D', 500);
    symbolMap.put('M', 1000);

    int n = s.length();
    int total = 0;
    int i = 0;

    while (i < n) {
      if (
        i < n - 1 && symbolMap.get(s.charAt(i)) < symbolMap.get(s.charAt(i + 1))
      ) {
        total += symbolMap.get(s.charAt(i + 1)) - symbolMap.get(s.charAt(i));
        i += 2;
      } else {
        total += symbolMap.get(s.charAt(i));
        i++;
      }
    }

    return total;
  }
}
