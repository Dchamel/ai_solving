"""Tests for LeetCode 387. First Unique Character in a String."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("a", 0),
        ("aa", -1),
        ("ab", 0),
        ("aba", 1),  # b is unique at index 1
        ("abcabc", -1),
        ("abcab", 2),  # c is unique at index 2
        ("z", 0),
        ("aabbc", 4),
        ("aabcc", 2),  # b is unique at index 2
    ],
)
def test_first_uniq_char(s: str, expected: int) -> None:
    assert Solution().firstUniqChar(s) == expected
