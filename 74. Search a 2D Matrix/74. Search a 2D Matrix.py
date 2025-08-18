from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            mid_i = mid // n
            mid_j = mid % n
            mid_matrix = matrix[mid_i][mid_j]

            if mid_matrix == target:
                return True
            elif mid_matrix > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
