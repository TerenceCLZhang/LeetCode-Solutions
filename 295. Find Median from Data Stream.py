class MedianFinder:

    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left) + 1:
            val = -heapq.heappop(self.right)
            heapq.heappush(self.left, val)

    def findMedian(self) -> float:
        l = len(self.left)
        r = len(self.right)

        if l > r:
            return -self.left[0]
        if r > l:
            return self.right[0]

        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
