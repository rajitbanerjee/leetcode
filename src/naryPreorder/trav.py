"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stk = [root]

        if not root:
            return []

        while stk:
            node = stk.pop()
            res.append(node.val)
            # add children to stack (reverse so that first child is at top of stk)
            stk.extend(node.children[::-1])

        return res
