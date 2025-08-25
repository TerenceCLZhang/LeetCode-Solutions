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

  int res;
  int count;

  public int kthSmallest(TreeNode root, int k) {
    count = k;
    dfs(root);
    return res;
  }

  private void dfs(TreeNode node) {
    if (node == null || count == 0) {
      return;
    }

    dfs(node.left);

    count--;
    if (count == 0) {
      res = node.val;
      return;
    }

    dfs(node.right);
  }
}
