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
 * @return {boolean}
 */
var isBalanced = function (root) {
  const dfs = (node) => {
    if (!node) {
      return 0;
    }

    const leftH = dfs(node.left);
    if (leftH === -1) {
      return -1;
    }

    const rightH = dfs(node.right);
    if (rightH === -1) {
      return -1;
    }

    if (Math.abs(leftH - rightH) > 1) {
      return -1;
    }

    return 1 + Math.max(leftH, rightH);
  };

  return dfs(root) !== -1;
};
