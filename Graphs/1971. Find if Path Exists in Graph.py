class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        stack = [source]

        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node not in visited:
                visited.add(node)
                for next_node in graph[node]:
                    stack.append(next_node)
        
        return False

# Time: O(n + e)
# Space: O(n + e)