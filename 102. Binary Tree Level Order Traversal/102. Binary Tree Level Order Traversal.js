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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) {
    return [];
  }

  const res = [];
  const q = [root];

  while (q.length > 0) {
    level_length = q.length;
    level = [];

    for (let i = 0; i < level_length; i++) {
      const n = q.shift();
      level.push(n.val);

      if (n.left) {
        q.push(n.left);
      }

      if (n.right) {
        q.push(n.right);
      }
    }

    res.push(level);
  }

  return res;
};
