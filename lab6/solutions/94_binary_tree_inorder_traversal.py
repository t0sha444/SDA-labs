from typing import List, Optional


# LeetCode provides TreeNode with fields val, left, and right.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.val)
            visit(node.right)

        visit(root)
        return result
