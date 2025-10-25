/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
  const maxHeap = new MaxPriorityQueue();

  for (stone of stones) {
    maxHeap.enqueue(stone);
  }

  while (maxHeap.size() > 1) {
    let largest = maxHeap.dequeue();
    const secondLargest = maxHeap.dequeue();

    if (largest !== secondLargest) {
      largest -= secondLargest;
      maxHeap.enqueue(largest);
    }
  }

  return maxHeap.size() === 0 ? 0 : maxHeap.front();
};
