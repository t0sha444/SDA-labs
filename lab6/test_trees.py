import importlib.util
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "algorithms"))

from binary_search_tree import TreeNode, insert, inorder, level_order


class LeetCodeTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def load_solution(filename, module_name):
    path = ROOT / "lab6" / "solutions" / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    module.TreeNode = LeetCodeTreeNode
    spec.loader.exec_module(module)
    return module.Solution()


def tree_snapshot(root, value_attr="value"):
    """Capture values and link identities to ensure traversals are read-only."""
    if root is None:
        return ()
    return (
        id(root), getattr(root, value_attr),
        id(root.left) if root.left is not None else None,
        id(root.right) if root.right is not None else None,
        tree_snapshot(root.left, value_attr),
        tree_snapshot(root.right, value_attr),
    )


def build_lecture_tree():
    root = None
    for value in [4, 2, 7, 1, 3, 6, 9]:
        root = insert(root, value)
    return root


def build_non_bst_tree(node_class=TreeNode):
    #       2
    #      / \
    #     1   3
    #    /
    #   4
    root = node_class(2)
    root.left = node_class(1)
    root.right = node_class(3)
    root.left.left = node_class(4)
    return root


def leetcode_inorder_values(root):
    if root is None:
        return []
    return leetcode_inorder_values(root.left) + [root.val] + leetcode_inorder_values(root.right)


class TestLab6(unittest.TestCase):
    def test_local_bst_build_and_duplicate(self):
        root = None
        for value in [4, 2, 7, 1, 3, 6, 9]:
            root = insert(root, value)
        self.assertEqual(inorder(root), [1, 2, 3, 4, 6, 7, 9])

        old_root = root
        root = insert(root, 6)
        self.assertIs(root, old_root)
        self.assertEqual(inorder(root), [1, 2, 3, 4, 6, 7, 9])

        fresh = build_lecture_tree()
        fresh = insert(fresh, 5)
        self.assertEqual(inorder(fresh), [1, 2, 3, 4, 5, 6, 7, 9])
        self.assertEqual(fresh.right.left.left.value, 5)

    def test_local_bst_edge_cases(self):
        self.assertEqual(inorder(None), [])
        root = insert(None, -4)
        root = insert(root, 0)
        root = insert(root, -9)
        self.assertEqual(inorder(root), [-9, -4, 0])

        chain = None
        for value in [1, 2, 3, 4]:
            chain = insert(chain, value)
        self.assertIsNone(chain.left)
        self.assertEqual(chain.right.value, 2)
        self.assertEqual(chain.right.right.value, 3)
        self.assertEqual(chain.right.right.right.value, 4)

    def test_leetcode_701_insert(self):
        solution = load_solution("701_insert_into_bst.py", "solution_701")
        root = None
        for value in [4, 2, 7, 1, 3, 6, 9]:
            root = solution.insertIntoBST(root, value)
        self.assertEqual(leetcode_inorder_values(root), [1, 2, 3, 4, 6, 7, 9])
        root = solution.insertIntoBST(root, 5)
        self.assertEqual(leetcode_inorder_values(root), [1, 2, 3, 4, 5, 6, 7, 9])

    def test_leetcode_94_and_local_inorder(self):
        solution = load_solution("94_binary_tree_inorder_traversal.py", "solution_94")
        root = build_non_bst_tree(LeetCodeTreeNode)
        before = tree_snapshot(root, "val")
        self.assertEqual(solution.inorderTraversal(root), [4, 1, 2, 3])
        self.assertEqual(tree_snapshot(root, "val"), before)
        self.assertEqual(solution.inorderTraversal(None), [])
        self.assertEqual(solution.inorderTraversal(LeetCodeTreeNode(7)), [7])

        self.assertEqual(inorder(build_lecture_tree()), [1, 2, 3, 4, 6, 7, 9])
        self.assertEqual(inorder(None), [])

    def test_leetcode_102_and_local_bfs(self):
        solution = load_solution("102_binary_tree_level_order_traversal.py", "solution_102")
        bst = LeetCodeTreeNode(4)
        bst.left = LeetCodeTreeNode(2)
        bst.right = LeetCodeTreeNode(7)
        bst.left.left = LeetCodeTreeNode(1)
        bst.left.right = LeetCodeTreeNode(3)
        bst.right.left = LeetCodeTreeNode(6)
        bst.right.right = LeetCodeTreeNode(9)
        before = tree_snapshot(bst, "val")
        self.assertEqual(solution.levelOrder(bst), [[4], [2, 7], [1, 3, 6, 9]])
        self.assertEqual(tree_snapshot(bst, "val"), before)
        self.assertEqual(solution.levelOrder(None), [])
        self.assertEqual(solution.levelOrder(LeetCodeTreeNode(5)), [[5]])

        self.assertEqual(level_order(build_lecture_tree()), [[4], [2, 7], [1, 3, 6, 9]])
        self.assertEqual(level_order(None), [])

    def test_traversals_non_bst_chains_and_unchanged_links(self):
        root = build_non_bst_tree()
        before = tree_snapshot(root)
        self.assertEqual(inorder(root), [4, 1, 2, 3])
        self.assertEqual(level_order(root), [[2], [1, 3], [4]])
        self.assertEqual(tree_snapshot(root), before)

        left_chain = TreeNode(3)
        left_chain.left = TreeNode(2)
        left_chain.left.left = TreeNode(1)
        self.assertEqual(inorder(left_chain), [1, 2, 3])
        self.assertEqual(level_order(left_chain), [[3], [2], [1]])

        right_chain = TreeNode(1)
        right_chain.right = TreeNode(2)
        right_chain.right.right = TreeNode(3)
        self.assertEqual(inorder(right_chain), [1, 2, 3])
        self.assertEqual(level_order(right_chain), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
