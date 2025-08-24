# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(p, q):
            if not p and not q:
                return True

            if not p and q or p and not q or p.val != q.val:
                return False

            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        def has_subtree(p):
            if not p:
                return False

            if is_same_tree(p, subRoot):
                return True

            return has_subtree(p.left) or has_subtree(p.right)

        return has_subtree(root)
