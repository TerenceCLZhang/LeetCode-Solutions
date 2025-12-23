class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj_list[node]:
                if nei != prev and not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
