/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

  public boolean isSymmetric(TreeNode root) {
    return checkSame(root.left, root.right);
  }

  private boolean checkSame(TreeNode leftNode, TreeNode rightNode) {
    if (leftNode == null && rightNode == null) {
      return true;
    }

    if (
      (leftNode == null && rightNode != null) ||
      (leftNode != null && rightNode == null) ||
      leftNode.val != rightNode.val
    ) {
      return false;
    }

    return (
      checkSame(leftNode.left, rightNode.right) &&
      checkSame(leftNode.right, rightNode.left)
    );
  }
}
