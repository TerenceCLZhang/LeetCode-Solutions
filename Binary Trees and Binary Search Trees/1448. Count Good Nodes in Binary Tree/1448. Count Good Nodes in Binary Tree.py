# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getGoodNodes(root, curr_max):
            if not root:
                return 0

            if root.val >= curr_max:
                return 1 + getGoodNodes(root.left, root.val) + getGoodNodes(root.right, root.val)

            return getGoodNodes(root.left, curr_max) + getGoodNodes(root.right, curr_max)
        
        return getGoodNodes(root, -float("inf"))

# Time: O(n)
# Space: O(n)