from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        ans = []
        visiting, visited = set(), set()

        def dfs(currentCourse):
            if currentCourse in visiting:
                return False

            if currentCourse in visited:
                return True

            visiting.add(currentCourse)

            for course in adj_list[currentCourse]:
                if not dfs(course):
                    return False

            visiting.remove(currentCourse)
            visited.add(currentCourse)
            ans.append(currentCourse)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return ans
