# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        # preorder traversal
        def helper(node: TreeNode):
            if node:
                self.s += str(node.val)
                if not node.left and node.right:
                    self.s += "()"
                elif node.left:
                    self.s += "("
                    helper(node.left)
                    self.s += ")"
                if node.right:
                    self.s += "("
                    helper(node.right)
                    self.s += ")"

        self.s = ""
        helper(t)
        return self.s
