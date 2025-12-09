class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        original = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while queue:
            cr, cc = queue.pop()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image