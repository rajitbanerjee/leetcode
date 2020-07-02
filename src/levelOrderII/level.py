# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return None
        res, queue = [], []
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            while size:
                # contruct current level
                node = queue.pop(0)
                level.append(node.val)
                # add child nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            # insert levels in reverse order
            res.insert(0, level)
        return res
