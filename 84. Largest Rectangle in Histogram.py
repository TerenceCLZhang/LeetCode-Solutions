class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            last_i = i
            while stack and stack[-1][0] > h:
                prev_h, prev_i = stack.pop()
                area = prev_h * (i - prev_i)
                max_area = max(max_area, area)
                last_i = prev_i

            stack.append((h, last_i))

        while stack:
            prev_h, prev_i = stack.pop()
            area = prev_h * (len(heights) - prev_i)
            max_area = max(max_area, area)

        return max_area
