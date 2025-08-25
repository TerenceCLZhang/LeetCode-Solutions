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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  res = null;
  count = k;

  const dfs = (node) => {
    if (!node || res) {
      return;
    }

    dfs(node.left);

    count--;
    if (count == 0) {
      res = node.val;
      return;
    }

    dfs(node.right);
  };

  dfs(root);
  return res;
};
