# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        total = 0
        # if node value is within range, add to total
        if L <= root.val <= R:
            total += root.val
        # repeat process for sub-trees
        total += self.rangeSumBST(root.left, L, R)
        total += self.rangeSumBST(root.right, L, R)
        return total
