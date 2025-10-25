import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

class Solution {

  public int networkDelayTime(int[][] times, int n, int k) {
    Map<Integer, List<int[]>> adjList = new HashMap<>();
    for (int[] t : times) {
      int source = t[0], target = t[1], time = t[2];
      adjList
        .computeIfAbsent(source, x -> new ArrayList<>())
        .add(new int[] { target, time });
    }

    int delay = 0;

    Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    minHeap.add(new int[] { 0, k });

    Set<Integer> visited = new HashSet<>();

    while (!minHeap.isEmpty()) {
      int[] pair = minHeap.poll();
      int time = pair[0], node = pair[1];

      if (visited.contains(node)) {
        continue;
      }

      visited.add(node);
      delay = Math.max(delay, time);

      if (adjList.containsKey(node)) {
        for (int[] pair2 : adjList.get(node)) {
          int node2 = pair2[0], time2 = pair2[1];
          if (!visited.contains(node2)) {
            minHeap.add(new int[] { time + time2, node2 });
          }
        }
      }
    }

    return visited.size() == n ? delay : -1;
  }
}
