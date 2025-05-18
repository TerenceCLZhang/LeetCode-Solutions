
# Left right arrays method
class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = max_r = 0
        n = len(height)
        max_h_left = [0] * n
        max_h_right = [0] * n

        summ = 0

        for i in range(n):
            max_h_left[i] = max_l
            max_l = max(max_l, height[i])
        
        for i in range(n - 1, -1, -1):
            max_h_right[i] = max_r
            max_r = max(max_r, height[i])
        
        for i in range(n):
            h = min(max_h_left[i], max_h_right[i]) - height[i]
            summ += max(h, 0)

        return summ

# Time: O(n)
# Space: O(n)


# Two pointer method

class Solution:
    def trap(self, height: List[int]) -> int:
        summ = 0
        l = 0
        r = len(height) - 1

        left_max = right_max = 0

        while l <= r:
            if height[l] < height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    summ += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    summ += right_max - height[r]
                r -= 1
        
        return summ

# Time: O(n)
# Space: O(1)