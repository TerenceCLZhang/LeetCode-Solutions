# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        max_level_sum = float("-inf")
        max_level = level

        queue = deque([root])

        while queue:
            level += 1
            curr_level_sum = 0

            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if curr_level_sum > max_level_sum:
                max_level_sum = curr_level_sum
                max_level = level

        return max_level
