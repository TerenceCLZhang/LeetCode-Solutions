# Can modify matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        ans = []

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while len(ans) < rows * cols:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
                matrix[top][i] = "."
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
                matrix[i][right] = "."
            right -= 1

            for i in range(right, left - 1, -1):
                if matrix[bottom][i] == ".": break
                ans.append(matrix[bottom][i])
                matrix[bottom][i] = "."
            bottom -= 1

            for i in range(bottom, top -1, -1):
                if matrix[i][left] == ".": break
                ans.append(matrix[i][left])
                matrix[i][left] = "."
            left += 1

        return ans


# Cannot modify matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        ans = []

        i = j = 0

        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        direction = RIGHT

        top_boundary = 0
        bottom_boundary = rows
        left_boundary = -1
        right_boundary = cols

        while len(ans) < rows * cols:
            if direction == RIGHT:
                while j < right_boundary:
                    ans.append(matrix[i][j])
                    j += 1
                i += 1
                j -= 1
                right_boundary -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < bottom_boundary:
                    ans.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                bottom_boundary -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > left_boundary:
                    ans.append(matrix[i][j])
                    j -= 1
                i -= 1
                j += 1
                left_boundary += 1
                direction = UP
            
            else:
                while i > top_boundary:
                    ans.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                top_boundary += 1
                direction = RIGHT

        return ans


# Time: O(n * m)
# Space: O(1)