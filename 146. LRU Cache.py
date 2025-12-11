class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.left_dummy = Node()
        self.right_dummy = Node()
        self.left_dummy.right = self.right_dummy
        self.right_dummy.left = self.left_dummy

    def add(self, node):
        old_mru = self.right_dummy.left
        self.right_dummy.left = node
        node.right = self.right_dummy
        old_mru.right = node
        node.left = old_mru

    def remove(self, node):
        lru = self.left_dummy.right
        self.left_dummy.right = lru.right
        lru.right.left = self.left_dummy

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            new_node = Node(key, value)
            self.map[key] = new_node
            self.add(new_node)

        if len(self.map) > self.capacity:
            lru = self.left_dummy.right
            self.remove(lru)
            del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
