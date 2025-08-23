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
var isSymmetric = function (root) {
  const checkSame = (leftNode, rightNode) => {
    if (!leftNode && !rightNode) {
      return true;
    }

    if (
      (!leftNode && rightNode) ||
      (leftNode && !rightNode) ||
      leftNode.val !== rightNode.val
    ) {
      return false;
    }

    return (
      checkSame(leftNode.left, rightNode.right) &&
      checkSame(leftNode.right, rightNode.left)
    );
  };

  return checkSame(root.left, root.right);
};
