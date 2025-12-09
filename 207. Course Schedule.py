class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)

        visit = set()

        def dfs(node):
            if node in visit:
                return False

            if adj_list[node] == []:
                return True

            visit.add(node)

            for nei in adj_list[node]:
                if not dfs(nei):
                    return False

            adj_list[node] = []
            visit.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
