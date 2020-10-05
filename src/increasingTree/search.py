# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inOrd = []

        def trav(root) -> None:
            if root:
                trav(root.left)
                inOrd.append(root)
                trav(root.right)
        trav(root)

        for i in range(len(inOrd)-1):
            inOrd[i].left = None
            inOrd[i].right = inOrd[i + 1]
        return inOrd[0]
