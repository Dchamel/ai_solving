"""LeetCode 257. Binary Tree Paths (Easy)

Given the root of a binary tree, return all root-to-leaf paths in any order,
each as a string "1->2->3".
"""

from __future__ import annotations
from typing import Optional


# Definition for a binary tree node (as on LeetCode).
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        result: list[str] = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if node is None:
                return
            cur = path + ("->" if path else "") + str(node.val)
            if node.left is None and node.right is None:
                result.append(cur)
                return
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, "")
        return result
