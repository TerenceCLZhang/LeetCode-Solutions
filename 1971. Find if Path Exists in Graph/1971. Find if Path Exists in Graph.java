import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

class Solution {

  public boolean validPath(int n, int[][] edges, int source, int destination) {
    Map<Integer, List<Integer>> adjList = new HashMap<>();

    for (int[] e : edges) {
      int u = e[0], v = e[1];

      adjList.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
      adjList.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
    }

    Set<Integer> seen = new HashSet<>();
    seen.add(source);
    Stack<Integer> stack = new Stack<>();
    stack.add(source);

    while (!stack.isEmpty()) {
      int node = stack.pop();

      if (node == destination) {
        return true;
      }

      for (int nei : adjList.getOrDefault(node, Collections.emptyList())) {
        if (!seen.contains(nei)) {
          seen.add(nei);
          stack.add(nei);
        }
      }
    }

    return false;
  }
}
