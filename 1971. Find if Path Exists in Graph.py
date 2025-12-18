class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        if source not in adj_list or destination not in adj_list:
            return False

        visited = set([source])

        def dfs(node):
            if node == destination:
                return True

            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    if dfs(nei):
                        return True

            return False

        return dfs(source)
