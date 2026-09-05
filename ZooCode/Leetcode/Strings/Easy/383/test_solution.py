"""Tests for LeetCode 383. Ransom Note."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "ransom,magazine,expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "", True),
        ("a", "a", True),
        ("abc", "cbad", True),
        ("abc", "ab", False),
        ("hello", "helloworld", True),
        ("hello", "world", False),
        ("aabb", "bbaa", True),
        ("aabb", "bba", False),
        ("x", "xyz", True),
    ],
)
def test_can_construct(ransom: str, magazine: str, expected: bool) -> None:
    assert Solution().canConstruct(ransom, magazine) is expected
