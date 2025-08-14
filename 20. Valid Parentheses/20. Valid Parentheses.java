import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {

  public boolean isValid(String s) {
    Map<Character, Character> parentheses = new HashMap<>();
    parentheses.putIfAbsent(')', '(');
    parentheses.putIfAbsent(']', '[');
    parentheses.putIfAbsent('}', '{');

    Stack<Character> stack = new Stack<>();

    for (char c : s.toCharArray()) {
      if (parentheses.containsKey(c)) {
        if (stack.isEmpty()) {
          return false;
        }

        char popped = stack.pop();
        if (popped != parentheses.get(c)) {
          return false;
        }
      } else {
        stack.add(c);
      }
    }

    return stack.isEmpty();
  }
}
