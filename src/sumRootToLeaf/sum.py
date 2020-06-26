# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Recursively traverse the tree nodes while finding the sum
        def findSum(node: TreeNode, total: str) -> int:
            if not node:
                return 0
            t = total + str(node.val)
            if not (node.right or node.left):
                # leaf node reached
                return int(t)
            else:
                # keep traversing the tree
                return findSum(node.right, t) + findSum(node.left, t)

        return findSum(root, "")
