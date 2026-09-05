"""Tests for LeetCode 389. Find the Difference."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("a", "aa", "a"),
        ("ae", "aea", "a"),
        ("xyz", "zyxa", "a"),
        ("hello", "lolleh", "l"),
        ("abc", "cbad", "d"),
        ("", "z", "z"),
        ("zz", "zzz", "z"),
    ],
)
def test_find_the_difference(s: str, t: str, expected: str) -> None:
    assert Solution().findTheDifference(s, t) == expected
