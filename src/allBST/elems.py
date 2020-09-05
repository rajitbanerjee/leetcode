# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def inOrder(root: TreeNode) -> None:
            if root:
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)

        inOrder(root1)
        inOrder(root2)

        return sorted(res)
