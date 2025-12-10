# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        def dfs(p_start, p_end, i_start, i_end):
            if p_start > p_end or i_start > i_end:
                return
            
            root_val = preorder[p_start]
            mid = inorder_index[root_val]
            left_size = mid - i_start

            root = TreeNode(root_val)

            root.left = dfs(p_start + 1, p_start + left_size, i_start, mid - 1)
            root.right = dfs(p_start + left_size + 1, p_end, mid + 1, i_end)

            return root
        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)