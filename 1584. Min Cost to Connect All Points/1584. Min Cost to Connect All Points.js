/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function (points) {
  const n = points.length;
  let cost = 0;
  const seen = new Set();
  const minHeap = new MinPriorityQueue({ compare: (a, b) => a[0] - b[0] });
  minHeap.enqueue([0, 0]);

  while (seen.size < n) {
    const [dist, i] = minHeap.dequeue();

    if (seen.has(i)) {
      continue;
    }

    seen.add(i);
    cost += dist;

    const [x, y] = points[i];

    for (let j = 0; j < n; j++) {
      if (!seen.has(j)) {
        const [otherX, otherY] = points[j];
        const manDist = Math.abs(x - otherX) + Math.abs(y - otherY);
        minHeap.enqueue([manDist, j]);
      }
    }
  }

  return cost;
};
