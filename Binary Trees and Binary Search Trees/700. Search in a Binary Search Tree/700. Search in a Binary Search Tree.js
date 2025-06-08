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
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function (root, val) {
  const search = (root) => {
    if (!root) return null;

    if (root.val === val) return root;
    else if (root.val < val) return search(root.right);
    else return search(root.left);
  };

  return search(root);
};

// Time: O(n)
// Space: O(n)
