from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set([source])
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for nei in adj_list[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        return False
