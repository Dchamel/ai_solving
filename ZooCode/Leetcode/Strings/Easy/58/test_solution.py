"""Tests for LeetCode 58. Length of Last Word."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        (" a", 1),
        ("a ", 1),
        ("   ", 0),
        ("day", 3),
        ("hello  ", 5),
        ("  hello   world  ", 5),
    ],
)
def test_length_of_last_word(s: str, expected: int) -> None:
    assert Solution().lengthOfLastWord(s) == expected
