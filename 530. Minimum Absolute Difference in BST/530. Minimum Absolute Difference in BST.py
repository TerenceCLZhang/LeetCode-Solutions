# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev = None

        def dfs(node):
            if not node or self.min_diff == 1:
                return

            dfs(node.left)

            if self.prev:
                self.min_diff = min(self.min_diff, abs(self.prev - node.val))

            self.prev = node.val

            dfs(node.right)

        dfs(root)
        return self.min_diff
