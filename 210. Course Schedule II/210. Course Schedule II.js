/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
  const adjList = new Map();
  for (const [course, prereq] of prerequisites) {
    if (!adjList.has(course)) {
      adjList.set(course, []);
    }
    adjList.get(course).push(prereq);
  }

  const ans = [];

  const visiting = new Set();
  const visited = new Set();

  const dfs = (currentCourse) => {
    if (visiting.has(currentCourse)) {
      return false;
    }

    if (visited.has(currentCourse)) {
      return true;
    }

    visiting.add(currentCourse);

    if (adjList.has(currentCourse)) {
      for (const course of adjList.get(currentCourse)) {
        if (!dfs(course)) {
          return false;
        }
      }
    }

    visiting.delete(currentCourse);
    visited.add(currentCourse);
    ans.push(currentCourse);
    return true;
  };

  for (let course = 0; course < numCourses; course++) {
    if (!dfs(course)) {
      return [];
    }
  }

  return ans;
};
