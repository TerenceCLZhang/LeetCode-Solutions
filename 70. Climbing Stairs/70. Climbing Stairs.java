class Solution {

  public int climbStairs(int n) {
    if (n <= 2) {
      return n;
    }

    int num1 = 1;
    int num2 = 2;

    for (int i = 3; i < n + 1; i++) {
      int temp = num2;
      num2 = num1 + num2;
      num1 = temp;
    }

    return num2;
  }
}
