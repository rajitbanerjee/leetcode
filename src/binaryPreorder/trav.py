from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        stk = [root]

        while stk:
            node = stk.pop()
            res.append(node.val)

            children = []
            # reverse order so that left child stays on top (end) of stk
            if node.right:
                children.append(node.right)
            if node.left:
                children.append(node.left)

            stk.extend(children)

        return res
