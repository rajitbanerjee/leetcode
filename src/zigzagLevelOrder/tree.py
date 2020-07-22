# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        if not root:
            return None
        res, queue = [], []

        queue.append(root)

        zig = 1
        while queue:
            size = len(queue)
            level = []

            # construct current level
            while size:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1

            # add level to result in zig-zag fashion
            if zig == -1:
                res.append(level[::-1])
            else:
                res.append(level)
            zig = -zig
        return res
