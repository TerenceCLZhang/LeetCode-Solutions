# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            length = len(queue)
            level_last = None

            for _ in range(length):
                curr = queue.popleft()
                level_last = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(level_last.val)

        return ans
