# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(node, summ):
            if not node:
                return False

            summ += node.val

            if not node.left and not node.right:
                return summ == targetSum

            left_sum = has_sum(node.left, summ)
            right_sum = has_sum(node.right, summ)

            return left_sum or right_sum

        return has_sum(root, 0)
