/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
  const maxHeap = new MaxPriorityQueue();

  for (const s of stones) {
    maxHeap.enqueue(s);
  }

  while (maxHeap.size() > 1) {
    const x = maxHeap.dequeue();
    const y = maxHeap.dequeue();

    if (x !== y) {
      maxHeap.enqueue(x - y);
    }
  }

  return maxHeap.size() > 0 ? maxHeap.front() : 0;
};

// Time: O(n log n)
// Space: O(n)
