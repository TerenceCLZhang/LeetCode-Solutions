# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def getLeaf(root, arr):
            if not root.left and not root.right:
                arr.append(root.val)
            
            if root.left:
                getLeaf(root.left, arr)
            if root.right:
                getLeaf(root.right, arr)
        
        getLeaf(root1, leaf1) 
        getLeaf(root2, leaf2)

        return leaf1 == leaf2

# Time: O(n + m)
# Space: O(n + m)