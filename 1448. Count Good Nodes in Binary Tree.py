# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_good = 0

        def dfs(node, max_node_val):
            if not node:
                return

            if node.val >= max_node_val:
                self.num_good += 1
                max_node_val = node.val

            dfs(node.left, max_node_val)
            dfs(node.right, max_node_val)

        dfs(root, float("-inf"))
        return self.num_good
