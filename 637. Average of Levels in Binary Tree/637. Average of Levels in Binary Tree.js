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
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  const q = [root];
  const res = [];

  while (q.length > 0) {
    const levelLength = q.length;
    let levelSum = 0;
    
    for (let i = 0; i < levelLength; i++) {
      const node = q.shift();
      levelSum += node.val;

      if (node.left) {
        q.push(node.left);
      }

      if (node.right) {
        q.push(node.right);
      }
    }

    res.push(levelSum / levelLength);
  }

  return res;
};
