# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest = 0
        self.k = k

        def dfs(node):
            if not node or self.k <= 0:
                return

            dfs(node.left)

            if self.k == 0:
                return

            self.k_smallest = node.val
            self.k -= 1

            dfs(node.right)

        dfs(root)
        return self.k_smallest
