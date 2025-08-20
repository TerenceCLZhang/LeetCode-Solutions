import java.util.Arrays;

class Solution {

  public int minEatingSpeed(int[] piles, int h) {
    int low = 1;
    int high = Arrays.stream(piles).max().getAsInt();

    while (low < high) {
      int mid = (low + high) / 2;

      int hours = 0;
      for (int pile : piles) {
        hours += pile / mid;
        if (pile % mid != 0) {
          hours++;
        }
      }

      if (hours <= h) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return low;
  }
}
