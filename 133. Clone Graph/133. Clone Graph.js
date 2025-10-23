/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function (node) {
  if (!node) {
    return;
  }

  const oldToNew = new Map();

  const dfs = (node) => {
    if (oldToNew.has(node)) {
      return oldToNew.get(node);
    }

    const copy = new Node((val = node.val));
    oldToNew.set(node, copy);

    for (const nei of node.neighbors) {
      copy.neighbors.push(dfs(nei));
    }

    return copy;
  };

  return dfs(node);
};
