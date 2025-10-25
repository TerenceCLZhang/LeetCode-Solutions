/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  const minHeap = new MinPriorityQueue();

  for (const n of nums) {
    minHeap.enqueue(n);
    if (minHeap.size() > k) {
      minHeap.dequeue();
    }
  }

  return minHeap.front();
};
