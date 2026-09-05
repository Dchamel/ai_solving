"""Tests for LeetCode 266. Palindrome Permutation."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("code", False),
        ("aab", True),
        ("carerac", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("abcba", True),
        ("abc", False),
        ("", True),
        ("aaa", True),
        ("aabb", True),
        ("aabbc", True),
        ("aabbcd", False),
        ("tactcoa", True),
    ],
)
def test_can_permute_palindrome(s: str, expected: bool) -> None:
    assert Solution().canPermutePalindrome(s) is expected
