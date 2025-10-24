import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

class Solution {

  public int minCostConnectPoints(int[][] points) {
    int n = points.length;
    int cost = 0;
    Set<Integer> seen = new HashSet<>();
    Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    minHeap.add(new int[] { 0, 0 });

    while (seen.size() < n) {
      int[] heapItem = minHeap.poll();
      int dist = heapItem[0];
      int i = heapItem[1];

      if (seen.contains(i)) {
        continue;
      }

      seen.add(i);
      cost += dist;

      int x = points[i][0];
      int y = points[i][1];

      for (int j = 0; j < n; j++) {
        if (!seen.contains(j)) {
          int otherX = points[j][0];
          int otherY = points[j][1];
          int manDist = Math.abs(x - otherX) + Math.abs(y - otherY);
          minHeap.add(new int[] { manDist, j });
        }
      }
    }

    return cost;
  }
}
