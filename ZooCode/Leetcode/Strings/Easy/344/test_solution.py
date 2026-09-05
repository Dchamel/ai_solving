"""Tests for LeetCode 344. Reverse String."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "input_list,expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        (["a", "b"], ["b", "a"]),
        (["a", "b", "c"], ["c", "b", "a"]),
        ([], []),
        (["1", "2", "3", "4", "5"], ["5", "4", "3", "2", "1"]),
    ],
)
def test_reverse_string(input_list: list[str], expected: list[str]) -> None:
    Solution().reverseString(input_list)
    assert input_list == expected
