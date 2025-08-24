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

  public boolean isSubtree(TreeNode root, TreeNode subRoot) {
    return hasSubtree(root, subRoot);
  }

  private boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null) {
      return true;
    }

    if (
      (p != null && q == null) || (p == null && q != null) || p.val != q.val
    ) {
      return false;
    }

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  }

  private boolean hasSubtree(TreeNode p, TreeNode subRoot) {
    if (p == null) {
      return false;
    }

    if (isSameTree(p, subRoot)) {
      return true;
    }

    return hasSubtree(p.left, subRoot) || hasSubtree(p.right, subRoot);
  }
}
