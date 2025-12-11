class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        edge_count = {}
        leaves = deque()
        for src, neighbors in adj_list.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbors)

        while leaves:
            if n <= 2:
                break

            for i in range(len(leaves)):
                curr = leaves.popleft()
                n -= 1
                for nei in adj_list[curr]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 1:
                        leaves.append(nei)

        return list(leaves)
