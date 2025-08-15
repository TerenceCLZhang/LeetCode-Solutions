import java.util.Stack;

class Solution {

  public int[] dailyTemperatures(int[] temperatures) {
    int n = temperatures.length;
    Stack<Integer> stack = new Stack<>();
    int[] ans = new int[n];

    for (int i = 0; i < n; i++) {
      while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
        int j = stack.pop();
        ans[j] = i - j;
      }
      stack.push(i);
    }

    return ans;
  }
}
