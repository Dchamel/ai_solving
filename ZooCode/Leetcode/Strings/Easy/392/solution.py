"""LeetCode 392. Is Subsequence (Easy)

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        # all() returns True if every char in s is found in the remaining
        # portion of the iterator (short-circuit on first miss).
        return all(ch in it for ch in s)
