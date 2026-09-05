"""Tests for LeetCode 242. Valid Anagram."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("abc", "cba", True),
        ("abc", "abd", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("aacc", "ccac", False),  # aacc: a2c2, ccac: c3a1 — not anagram
        ("aacc", "ccaa", True),   # both a2c2
        ("aab", "aba", True),
    ],
)
def test_is_anagram(s: str, t: str, expected: bool) -> None:
    assert Solution().isAnagram(s, t) is expected
