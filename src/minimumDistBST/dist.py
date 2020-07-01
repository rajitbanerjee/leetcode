# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []

        # traverse tree and store node values in list
        def trav(node) -> None:
            if node:
                nodes.append(node.val)
                trav(node.left)
                trav(node.right)
        trav(root)

        nodes.sort()
        minDiff = nodes[-1] - nodes[0]
        # compute the minimum difference between two nodes
        for i in range(len(nodes) - 1):
            diff = nodes[i + 1] - nodes[i]
            if diff < minDiff:
                minDiff = diff

        return minDiff
