"""Tests for LeetCode 171. Excel Sheet Column Number."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "column_title,expected",
    [
        ("A", 1),
        ("B", 2),
        ("Z", 26),
        ("AA", 27),
        ("AB", 28),
        ("AZ", 52),
        ("BA", 53),
        ("ZY", 701),
        ("ZZ", 702),
        ("AAA", 703),
        ("FXSHRXW", 2147483647),  # max 32-bit int
    ],
)
def test_title_to_number(column_title: str, expected: int) -> None:
    assert Solution().titleToNumber(column_title) == expected
