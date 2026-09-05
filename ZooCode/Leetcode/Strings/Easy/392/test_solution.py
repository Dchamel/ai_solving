"""Tests for LeetCode 392. Is Subsequence."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
        ("abc", "", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("bb", "ahbgdc", False),
        ("leetcode", "leetcde", False),
        ("abc", "abc", True),
        ("abc", "abxyc", True),
    ],
)
def test_is_subsequence(s: str, t: str, expected: bool) -> None:
    assert Solution().isSubsequence(s, t) is expected
