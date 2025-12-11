# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialize = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    serialize.append("#")
                else:
                    serialize.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)

        while serialize and serialize[-1] == "#":
            serialize.pop()

        return ",".join(serialize)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        data = [v for v in data.split(",")]

        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(data):
            curr = queue.popleft()

            if data[i] != "#":
                node = TreeNode(int(data[i]))
                curr.left = node
                queue.append(node)
            i += 1

            if i >= len(data):
                break

            if data[i] != "#":
                node = TreeNode(int(data[i]))
                curr.right = node
                queue.append(node)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
