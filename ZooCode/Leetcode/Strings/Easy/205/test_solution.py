"""Tests for LeetCode 205. Isomorphic Strings."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", True),
        ("ab", "aa", False),
        ("aa", "ab", False),
        ("abab", "baba", True),
        ("abab", "cdcd", True),
        ("ab", "cd", True),
    ],
)
def test_is_isomorphic(s: str, t: str, expected: bool) -> None:
    assert Solution().isIsomorphic(s, t) is expected
