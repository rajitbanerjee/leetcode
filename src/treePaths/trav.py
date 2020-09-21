from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def trav(root, path):
            if root:
                if not (root.left or root.right):
                    path.append(str(root.val))
                    res.append("->".join(path))
                    return
                trav(root.left, path + [str(root.val)])
                trav(root.right, path + [str(root.val)])
        trav(root, [])
        return res


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print("""Input: 
        1
      /   \\
     2     3
      \\
       5
    """)
    print(f"Output: {Solution().binaryTreePaths(root)}")
