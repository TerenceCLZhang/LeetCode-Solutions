/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function (times, n, k) {
  const adjList = new Map();
  for (const [source, target, time] of times) {
    if (!adjList.has(source)) {
      adjList.set(source, []);
    }
    adjList.get(source).push([target, time]);
  }

  let delay = 0;

  const minHeap = new MinPriorityQueue({ compare: (a, b) => a[0] - b[0] });
  minHeap.enqueue([0, k]);

  const visited = new Set();

  while (!minHeap.isEmpty()) {
    const [time, node] = minHeap.dequeue();

    if (visited.has(node)) {
      continue;
    }

    visited.add(node);
    delay = Math.max(time, delay);

    if (adjList.has(node)) {
      for (const [node2, time2] of adjList.get(node)) {
        if (!visited.has(node2)) {
          minHeap.enqueue([time + time2, node2]);
        }
      }
    }
  }

  return visited.size === n ? delay : -1;
};
