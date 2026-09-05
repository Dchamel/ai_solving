"""Tests for LeetCode 246. Strobogrammatic Number."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        ("69", True),
        ("88", True),
        ("818", True),
        ("2", False),
        ("1", True),
        ("0", True),
        ("8", True),
        ("6", False),
        ("9", False),
        ("11", True),
        ("00", True),
        ("619", True),
        ("101", True),
        ("609", True),
        ("689", True),  # 6->9, 8->8, 9->6, rotated reads "689"
        ("686", False),  # 6->9 but last is 6, not 9
        ("1001", True),
        ("962", False),
    ],
)
def test_is_strobogrammatic(num: str, expected: bool) -> None:
    assert Solution().isStrobogrammatic(num) is expected
