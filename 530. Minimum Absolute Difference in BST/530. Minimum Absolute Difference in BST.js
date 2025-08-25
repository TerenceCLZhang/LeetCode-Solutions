/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getMinimumDifference = function (root) {
  minDiff = Infinity;
  prev = null;

  const dfs = (node) => {
    if (!node || minDiff === 1) {
      return;
    }

    dfs(node.left);

    if (prev) {
      minDiff = Math.min(minDiff, Math.abs(prev - node.val));
    }

    prev = node.val;

    dfs(node.right);
  };

  dfs(root);
  return minDiff;
};
