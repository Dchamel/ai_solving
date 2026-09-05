"""Tests for LeetCode 345. Reverse Vowels of a String."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("a", "a"),
        ("ae", "ea"),
        ("AE", "EA"),
        ("aA", "Aa"),
        ("bcd", "bcd"),
        ("", ""),
        ("a.", "a."),
        (".a", ".a"),
        ("a.b", "a.b"),
        ("a.b.c", "a.b.c"),
        ("IceCreAm", "AceCreIm"),
        ("race car", "race car"),
    ],
)
def test_reverse_vowels(s: str, expected: str) -> None:
    assert Solution().reverseVowels(s) == expected
