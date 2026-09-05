"""Tests for LeetCode 13. Roman to Integer."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("I", 1),
        ("V", 5),
        ("IV", 4),
        ("IX", 9),
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMMCMXCIX", 3999),  # largest valid roman numeral
    ],
)
def test_roman_to_int(s: str, expected: int) -> None:
    assert Solution().romanToInt(s) == expected
