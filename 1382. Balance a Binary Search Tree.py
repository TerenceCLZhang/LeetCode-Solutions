# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def inorder_traversal(node):
            if not node:
                return
            
            inorder_traversal(node.left)
            inorder.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        
        def balance(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            root = TreeNode(inorder[mid])
            root.left = balance(left, mid - 1)
            root.right = balance(mid + 1, right)
            return root
        
        return balance(0, len(inorder) - 1)