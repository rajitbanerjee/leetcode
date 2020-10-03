"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        childDepths = [self.maxDepth(c) for c in root.children]
        return 1 + (0 if not childDepths else max(childDepths))
