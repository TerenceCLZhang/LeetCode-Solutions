import java.util.HashMap;
import java.util.Map;

class Solution {

  public int maxNumberOfBalloons(String text) {
    Map<Character, Integer> letters = new HashMap<>();
    letters.put('b', 0);
    letters.put('a', 0);
    letters.put('l', 0);
    letters.put('o', 0);
    letters.put('n', 0);

    for (char c : text.toCharArray()) {
      if (letters.containsKey(c)) {
        letters.put(c, letters.get(c) + 1);
      }
    }

    return Math.min(
      letters.get('b'),
      Math.min(
        letters.get('a'),
        Math.min(
          letters.get('l') / 2,
          Math.min(letters.get('o') / 2, letters.get('n'))
        )
      )
    );
  }
}
