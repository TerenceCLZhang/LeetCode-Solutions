# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []

        while queue:
            row_size = len(queue)
            summ = 0
            for _ in range(row_size):
                curr = queue.popleft()
                summ += curr.val

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            ans.append(summ / row_size)

        return ans
