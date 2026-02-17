class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.deleted = set()

    def popSmallest(self) -> int:
        ret = self.smallest
        self.deleted.add(ret)
        self.smallest += 1
        while self.smallest in self.deleted:
            self.smallest += 1
        return ret

    def addBack(self, num: int) -> None:
        if num in self.deleted:
            self.deleted.remove(num)
            if num < self.smallest:
                self.smallest = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
