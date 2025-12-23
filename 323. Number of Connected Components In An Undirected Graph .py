# DFS Solution

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(n):
            for nei in adj_list[n]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        ans = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                ans += 1

        return ans


# Union Find Solution

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]  # path compression
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1

        ans = n
        for n1, n2 in edges:
            ans -= union(n1, n2)

        return ans
