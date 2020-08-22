# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return None
        q, res = [root], []

        while q:
            level, size = [], len(q)

            while size:
                node = q.pop(0)
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1

            res.append(level)
        return res
