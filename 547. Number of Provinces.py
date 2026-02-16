class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        visited = set()

        for i in range(len(isConnected)):
            if i not in visited:
                num_provinces += 1
                queue = deque([i])
                visited.add(i)
                while queue:
                    curr = queue.popleft()
                    for nei in range(len(isConnected[curr])):
                        if isConnected[curr][nei] == 1 and nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

        return num_provinces
