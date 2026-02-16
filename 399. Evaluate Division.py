class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj_list[a].append((b, values[i]))
            adj_list[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj_list or target not in adj_list:
                return -1

            queue = deque([(src, 1)])
            visited = set([src])

            while queue:
                node, weight = queue.popleft()

                if node == target:
                    return weight

                for nei, w in adj_list[node]:
                    if nei not in visited:
                        queue.append((nei, w * weight))
                        visited.add(nei)

            return -1

        return [bfs(src, target) for src, target in queries]
