import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {

  public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> counter = new HashMap<>();

    for (int n : nums) {
      counter.put(n, counter.getOrDefault(n, 0) + 1);
    }

    PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
      (a, b) -> a.getValue() - b.getValue()
    );

    for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
      heap.add(entry);
      if (heap.size() > k) {
        heap.poll();
      }
    }

    int[] ans = new int[k];
    for (int i = 0; i < k; i++) {
      ans[i] = heap.poll().getKey();
    }

    return ans;
  }
}
