class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        ans = []
        visiting, visited = set(), set()

        def dfs(c):
            if c in visiting:
                return False

            if c in visited:
                return True

            visiting.add(c)

            for prereq in adj_list[c]:
                if not dfs(prereq):
                    return False

            visiting.remove(c)
            visited.add(c)
            ans.append(c)

            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []

        return ans
