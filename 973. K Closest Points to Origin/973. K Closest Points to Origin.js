/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
  const maxHeap = new MaxPriorityQueue({ compare: (a, b) => a[0] - b[0] });

  for (const p of points) {
    const dist = p[0] ** 2 + p[1] ** 2;
    maxHeap.enqueue([dist, p]);
    if (maxHeap.size() > k) {
      maxHeap.dequeue();
    }
  }

  const ans = [];
  while (!maxHeap.isEmpty()) {
    ans.push(maxHeap.dequeue()[1]);
  }
  return ans;
};
