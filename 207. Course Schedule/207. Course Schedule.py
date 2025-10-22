from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visitng = set()  # Set containing courses that we have visisted on our current DFS path

        def dfs(current_course):
            # Already seen this course in our path then we have a cycle
            if current_course in visitng:
                return False

            # If the current course has no prerequisites
            if current_course not in adj_list.keys():
                return True

            visitng.add(current_course)
            for prereq in adj_list[current_course]:
                if not dfs(prereq):
                    return False

            visitng.remove(current_course)
            # We know the current course can finish so we don't repeat work already done before
            adj_list[current_course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
