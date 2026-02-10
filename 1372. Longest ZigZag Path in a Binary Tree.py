# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node, is_left, curr_length):
            if not node:
                return

            if is_left:
                dfs(node.right, False, curr_length + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, curr_length + 1)
                dfs(node.right, False, 1)

            self.longest = max(self.longest, curr_length)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.longest
