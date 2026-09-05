"""Tests for LeetCode 20. Valid Parentheses."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("(((", False),
        ("(()", False),
        ("(())", True),
        ("{[()]}", True),
        ("{[(])}", False),
    ],
)
def test_is_valid(s: str, expected: bool) -> None:
    assert Solution().isValid(s) is expected
