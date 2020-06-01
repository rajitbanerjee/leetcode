package invertBinaryTree;

public class Invert {
    public TreeNode invertTree(TreeNode node) {
        if (node != null) {
            // Mirror sub-trees
            TreeNode left = invertTree(node.left);
            TreeNode right = invertTree(node.right);
            // Swap node's children
            node.left = right;
            node.right = left;
        }
        return node;
    }

    // Definition for a binary tree node.
    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}

