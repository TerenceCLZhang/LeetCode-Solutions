class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return

            visited.add(room)

            for r in rooms[room]:
                dfs(r)

        dfs(0)
        return len(visited) == len(rooms)
