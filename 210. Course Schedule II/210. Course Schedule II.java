import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {

  Map<Integer, List<Integer>> adjList;
  List<Integer> ansArrayList;
  Set<Integer> visiting;
  Set<Integer> visited;

  public int[] findOrder(int numCourses, int[][] prerequisites) {
    adjList = new HashMap<>();
    for (int[] pair : prerequisites) {
      adjList.computeIfAbsent(pair[0], k -> new ArrayList<>()).add(pair[1]);
    }

    ansArrayList = new ArrayList<>();

    visiting = new HashSet<>();
    visited = new HashSet<>();

    for (int course = 0; course < numCourses; course++) {
      if (!dfs(course)) {
        return new int[0];
      }
    }

    int[] ans = new int[numCourses];
    for (int i = 0; i < numCourses; i++) {
      ans[i] = ansArrayList.get(i);
    }
    return ans;
  }

  private boolean dfs(int currentCourse) {
    if (visiting.contains(currentCourse)) {
      return false;
    }

    if (visited.contains(currentCourse)) {
      return true;
    }

    visiting.add(currentCourse);

    if (adjList.containsKey(currentCourse)) {
      for (int course : adjList.get(currentCourse)) {
        if (!dfs(course)) {
          return false;
        }
      }
    }

    visiting.remove(currentCourse);
    visited.add(currentCourse);
    ansArrayList.add(currentCourse);
    return true;
  }
}
