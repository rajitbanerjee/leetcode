# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        if root.left:

            # add value for leaf nodes only
            if not (root.left.left or root.left.right):
                total += root.left.val

            total += self.sumOfLeftLeaves(root.left)
        if root.right:
            total += self.sumOfLeftLeaves(root.right)
        return total
