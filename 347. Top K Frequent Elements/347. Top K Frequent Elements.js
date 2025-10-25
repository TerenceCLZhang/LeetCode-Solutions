/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const counter = new Map();
  for (const n of nums) {
    counter.set(n, (counter.get(n) || 0) + 1);
  }

  const minHeap = new MinPriorityQueue({ compare: (a, b) => a[0] - b[0] });

  for (const [num, count] of counter.entries()) {
    minHeap.enqueue([count, num]);
    if (minHeap.size() > k) {
      minHeap.dequeue();
    }
  }

  const ans = [];
  while (!minHeap.isEmpty()) {
    ans.push(minHeap.dequeue()[1]);
  }
  return ans;
};
