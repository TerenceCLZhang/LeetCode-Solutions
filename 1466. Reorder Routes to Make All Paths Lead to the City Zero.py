class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set((a, b) for a, b in connections)
        neighbors = defaultdict(list)
        visited = set([0])
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visited, changes

            for nei in neighbors[city]:
                if nei not in visited:
                    if (city, nei) in edges:
                        changes += 1
                    visited.add(nei)
                    dfs(nei)

        dfs(0)
        return changes
