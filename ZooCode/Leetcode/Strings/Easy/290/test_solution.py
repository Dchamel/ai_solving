"""Tests for LeetCode 290. Word Pattern."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "pattern,s,expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("a", "a", True),
        ("a", "dog", True),
        ("ab", "dog cat", True),
        ("ab", "dog dog", False),
        ("aaa", "dog dog dog", True),
        ("abc", "dog cat fish", True),
        ("abba", "dog cat cat dog", True),
        ("abba", "x y y x", True),
        ("abba", "x y y z", False),
    ],
)
def test_word_pattern(pattern: str, s: str, expected: bool) -> None:
    assert Solution().wordPattern(pattern, s) is expected
