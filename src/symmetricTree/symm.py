# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p1: TreeNode, p2: TreeNode) -> bool:
            if not (p1 or p2):
                return True
            elif not (p1 and p2):
                return False
            else:
                return p1.val == p2.val and \
                    check(p1.left, p2.right) and \
                    check(p1.right, p2.left)

        if not root:
            return True
        return check(root.left, root.right)
