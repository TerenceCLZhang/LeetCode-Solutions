class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) 
        cols = len(matrix[0])

        l = 0
        h = rows * cols - 1

        while l <= h:
            m = (l + h) // 2

            i, j = divmod(m, cols)

            mid_val = matrix[i][j]
            if mid_val == target:
                return True
            elif mid_val < target:
                l += 1
            else:
                h -= 1

        return False

# Time: O(log(m * n))
# Space: O(1)