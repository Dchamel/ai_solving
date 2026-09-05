"""Tests for LeetCode 405. Convert a Number to Hexadecimal."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (26, "1a"),
        (-1, "ffffffff"),
        (0, "0"),
        (1, "1"),
        (15, "f"),
        (16, "10"),
        (255, "ff"),
        (256, "100"),
        (1000, "3e8"),
        (-2, "fffffffe"),
        (2147483647, "7fffffff"),
        (-2147483648, "80000000"),
        (4095, "fff"),
        (65535, "ffff"),
    ],
)
def test_to_hex(num: int, expected: str) -> None:
    assert Solution().toHex(num) == expected
