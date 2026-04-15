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
    private void dfs(TreeNode root, List<Integer> values){
        if (root == null)
            return;

        dfs(root.left, values);
        values.add(root.val);
        dfs(root.right, values);
    }

    public int kthSmallest(TreeNode root, int k) {
        var values = new ArrayList<Integer>();
        dfs(root, values);
        // System.out.println(values);
        return values.get(k - 1);
    }
}
