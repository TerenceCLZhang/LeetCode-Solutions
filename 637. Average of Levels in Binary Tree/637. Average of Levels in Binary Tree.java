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

  public List<Double> averageOfLevels(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);

    List<Double> res = new ArrayList<>();

    while (!q.isEmpty()) {
      int levelLength = q.size();
      double levelSum = 0;

      for (int i = 0; i < levelLength; i++) {
        TreeNode node = q.remove();
        levelSum += node.val;

        if (node.left != null) {
          q.add(node.left);
        }

        if (node.right != null) {
          q.add(node.right);
        }
      }

      res.add(levelSum / levelLength);
    }

    return res;
  }
}
