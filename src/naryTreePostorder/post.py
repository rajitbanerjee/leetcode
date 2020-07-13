# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list:
        ans = []

        def help(root):
            if root:
                for c in root.children:
                    help(c)
                ans.append(root.val)
        help(root)
        return ans
