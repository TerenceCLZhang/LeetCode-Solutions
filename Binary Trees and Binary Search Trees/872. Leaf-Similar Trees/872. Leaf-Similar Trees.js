/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function (root1, root2) {
  let leaf1 = [];
  let leaf2 = [];

  const getLeaf = (root, arr) => {
    if (!root.left && !root.right) arr.push(root.val);

    if (root.left) getLeaf(root.left, arr);
    if (root.right) getLeaf(root.right, arr);
  };

  getLeaf(root1, leaf1);
  getLeaf(root2, leaf2);

  return (
    leaf1.length === leaf2.length && leaf1.every((val, i) => val === leaf2[i])
  );
};

// Time: O(n + m)
// Space: O(n + m)
