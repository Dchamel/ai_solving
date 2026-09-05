"""Tests for LeetCode 125. Valid Palindrome."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("a.", True),
        ("0P", False),
        ("ab", False),
        ("aa", True),
        ("aba", True),
        ("aab", False),
        ("Madam, I'm Adam", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("12345", False),
    ],
)
def test_is_palindrome(s: str, expected: bool) -> None:
    assert Solution().isPalindrome(s) is expected
