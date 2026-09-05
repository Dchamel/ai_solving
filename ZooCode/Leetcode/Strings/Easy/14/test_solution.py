"""Tests for LeetCode 14. Longest Common Prefix."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["a"], "a"),
        (["", ""], ""),
        (["ab", "a"], "a"),
        (["abc", "abc", "abc"], "abc"),
        (["", "b"], ""),
        (["aaa", "aaa", "aa"], "aa"),
    ],
)
def test_longest_common_prefix(strs: list[str], expected: str) -> None:
    assert Solution().longestCommonPrefix(strs) == expected
