from collections import deque


class TreeNode:
    """Node used by the local BST and traversal exercises."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert value into a BST and return the (possibly new) subtree root.

    Duplicate values are ignored, as required by the local Lab 6 task.
    """
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    """Return values in recursive left-node-right DFS order."""
    result = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result


def level_order(root):
    """Return BFS values grouped by depth, visiting left before right."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result
