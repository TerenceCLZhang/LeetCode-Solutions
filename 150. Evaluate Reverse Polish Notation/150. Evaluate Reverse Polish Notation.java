import java.util.Stack;

class Solution {

  public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();

    for (String t : tokens) {
      if ("+-*/".contains(t)) {
        int val2 = stack.pop();
        int val1 = stack.pop();

        switch (t) {
          case "+":
            stack.add(val1 + val2);
            break;
          case "-":
            stack.add(val1 - val2);
            break;
          case "*":
            stack.add(val1 * val2);
            break;
          case "/":
            stack.add(val1 / val2);
            break;
          default:
            break;
        }
      } else {
        stack.add(Integer.parseInt(t));
      }
    }

    return stack.pop();
  }
}
