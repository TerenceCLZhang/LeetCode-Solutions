/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function (n, edges, source, destination) {
  const adjList = new Map();

  for (const [u, v] of edges) {
    if (!adjList.get(u)) {
      adjList.set(u, []);
    }

    if (!adjList.get(v)) {
      adjList.set(v, []);
    }

    adjList.get(u).push(v);
    adjList.get(v).push(u);
  }

  const seen = new Set();
  seen.add(source);
  const stack = [source];

  while (stack.length > 0) {
    const node = stack.pop();

    if (node === destination) {
      return true;
    }

    for (const nei of adjList.get(node) || []) {
      if (!seen.has(nei)) {
        seen.add(nei);
        stack.push(nei);
      }
    }
  }

  return false;
};
