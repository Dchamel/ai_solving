"""Tests for LeetCode 293. Flip Game."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("++++", ["--++", "+--+", "++--"]),
        ("++", ["--"]),
        ("--", []),
        ("+-", []),
        ("-+", []),
        ("", []),
        ("+", []),
        ("+++", ["--+", "+--"]),
        ("+++++", ["--+++", "+--++", "++--+", "+++--"]),
    ],
)
def test_generate_possible_next_moves(s: str, expected: list[str]) -> None:
    assert Solution().generatePossibleNextMoves(s) == expected


def test_minus_plus_plus_minus() -> None:
    # "-++-" -> flip the middle "++" -> "----"
    assert Solution().generatePossibleNextMoves("-++-") == ["----"]
