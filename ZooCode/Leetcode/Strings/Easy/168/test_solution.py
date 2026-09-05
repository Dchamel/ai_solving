"""Tests for LeetCode 168. Excel Sheet Column Title."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "column_number,expected",
    [
        (1, "A"),
        (26, "Z"),
        (27, "AA"),
        (28, "AB"),
        (52, "AZ"),
        (53, "BA"),
        (701, "ZY"),
        (702, "ZZ"),
        (703, "AAA"),
        (2147483647, "FXSHRXW"),  # max 32-bit int
    ],
)
def test_convert_to_title(column_number: int, expected: str) -> None:
    assert Solution().convertToTitle(column_number) == expected
