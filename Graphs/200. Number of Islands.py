# Cannot modify grid
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        islands = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                
                stack = [(i, j)]
                while stack:
                    ci, cj = stack.pop()
                    visited.add((cu, cj))

                    for di, dj in directions:
                        ni, nj = cu + di, cj + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1" and (ni, nj) not in visited:
                            stack.append((ni, nj))

                islands += 1
            
        return islands


# Can modify grid
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    stack = [(i, j)]
                    grid[i][j] = "0"  # Mark as visited
                    while stack:
                        ci, cj = stack.pop()
                        for di, dj in directions:
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "1":
                                grid[ni][nj] = "0"
                                stack.append((ni, nj))
                    islands += 1
        
        return islands


# Time: O(n * m)
# Space: O(n * m)