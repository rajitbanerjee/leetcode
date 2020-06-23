# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            # count right and left child nodes
            right = self.countNodes(root.right)
            left = self.countNodes(root.left)
            return 1 + left + right
