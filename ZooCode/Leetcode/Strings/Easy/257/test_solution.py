"""Tests for LeetCode 257. Binary Tree Paths."""
import pytest

from solution import Solution, TreeNode


def _build(values: list) -> TreeNode | None:
    """Build a binary tree from a level-order list (None for gaps)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def _paths(root: TreeNode | None) -> set[str]:
    return set(Solution().binaryTreePaths(root))


def test_single_node() -> None:
    assert _paths(_build([1])) == {"1"}


def test_two_levels_left() -> None:
    assert _paths(_build([1, 2])) == {"1->2"}


def test_two_levels_both() -> None:
    assert _paths(_build([1, 2, 3])) == {"1->2", "1->3"}


def test_example_1() -> None:
    #     1
    #    / \
    #   2   3
    #    \
    #     5
    assert _paths(_build([1, 2, 3, None, 5])) == {"1->2->5", "1->3"}


def test_left_chain() -> None:
    # 1 -> 2 -> 4
    root = TreeNode(1, TreeNode(2, TreeNode(4)))
    assert _paths(root) == {"1->2->4"}


def test_right_chain() -> None:
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert _paths(root) == {"1->2->3"}


def test_empty() -> None:
    assert _paths(None) == set()


def test_full_tree_depth_3() -> None:
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    assert _paths(_build([1, 2, 3, 4, 5, 6, 7])) == {
        "1->2->4",
        "1->2->5",
        "1->3->6",
        "1->3->7",
    }
