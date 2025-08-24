import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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

  public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();

    if (root == null) {
      return res;
    }

    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);

    while (!q.isEmpty()) {
      int levelLength = q.size();
      List<Integer> level = new ArrayList<>();

      for (int i = 0; i < levelLength; i++) {
        TreeNode n = q.remove();
        level.add(n.val);

        if (n.left != null) {
          q.add(n.left);
        }

        if (n.right != null) {
          q.add(n.right);
        }
      }

      res.add(level);
    }

    return res;
  }
}
