# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            # search left subtree if root is greater than both p, q
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            # search right subtree if root is smaller than both p, q
            return self.lowestCommonAncestor(root.right, p, q)
        # base case: root itself is the LCA
        return root
