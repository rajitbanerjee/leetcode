# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stk = [], []
        node = root
        while node or stk:
            while node:
                # keep going left and push nodes to stack
                stk.append(node)
                node = node.left
            node = stk.pop()
            res.append(node.val)
            node = node.right

        return res
