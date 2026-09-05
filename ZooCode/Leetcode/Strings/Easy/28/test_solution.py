"""Tests for LeetCode 28. Find the Index of the First Occurrence in a String."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "haystack,needle,expected",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("abc", "", 0),
        ("abc", "c", 2),
        ("abc", "abc", 0),
        ("abc", "abcd", -1),
        ("mississippi", "issip", 4),
    ],
)
def test_str_str(haystack: str, needle: str, expected: int) -> None:
    assert Solution().strStr(haystack, needle) == expected
