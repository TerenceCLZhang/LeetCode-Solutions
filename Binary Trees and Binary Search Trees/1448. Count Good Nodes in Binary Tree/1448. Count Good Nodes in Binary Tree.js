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
var goodNodes = function (root) {
  const getGoodNodes = (root, curr_max) => {
    if (!root) return 0;

    if (root.val >= curr_max) {
      return (
        1 +
        getGoodNodes(root.left, root.val) +
        getGoodNodes(root.right, root.val)
      );
    }
    return (
      getGoodNodes(root.left, curr_max) + getGoodNodes(root.right, curr_max)
    );
  };

  return getGoodNodes(root, -Infinity);
};

// Time: O(n)
// Space: O(n)