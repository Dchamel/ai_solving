"""Tests for LeetCode 67. Add Binary."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "0", "1"),
        ("0", "1", "1"),
        ("1", "1", "10"),
        ("111", "111", "1110"),
        ("100", "110010", "110110"),
        ("101111", "10", "110001"),
        ("11111111", "1", "100000000"),
    ],
)
def test_add_binary(a: str, b: str, expected: str) -> None:
    assert Solution().addBinary(a, b) == expected
