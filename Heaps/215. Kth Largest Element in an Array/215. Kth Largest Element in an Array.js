/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  nums = new MaxPriorityQueue();

  for (let num of nums) maxHeap.enqueue(num);

  for (let i = 0; i < k - 1; i++) maxHeap.dequeue();

  return maxHeap.front();
};

// Time: O(n + k log n)
// Space: O(n)
