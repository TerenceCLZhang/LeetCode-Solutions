class Solution {

  public int minCostClimbingStairs(int[] cost) {
    int num1 = 0, num2 = 0;

    for (int i = 2; i < cost.length + 1; i++) {
      int temp = num2;
      num2 = Math.min(num1 + cost[i - 2], num2 + cost[i - 1]);
      num1 = temp;
    }

    return num2;
  }
}
