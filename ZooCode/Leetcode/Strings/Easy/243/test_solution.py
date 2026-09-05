"""Tests for LeetCode 243. Shortest Word Distance."""
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "words,word1,word2,expected",
    [
        (
            ["practice", "makes", "perfect", "coding", "makes"],
            "coding",
            "practice",
            3,
        ),
        (
            ["practice", "makes", "perfect", "coding", "makes"],
            "makes",
            "coding",
            1,
        ),
        (["a", "b"], "a", "b", 1),
        (["a", "c", "b", "a"], "a", "b", 1),
        (["a", "b", "c", "d", "a"], "a", "d", 1),  # a@4, d@3 -> 1
        (["x", "y", "x", "y"], "x", "y", 1),
        (["a", "x", "x", "x", "b"], "a", "b", 4),
        (["a", "b", "b", "a"], "a", "b", 1),
    ],
)
def test_shortest_distance(
    words: list[str], word1: str, word2: str, expected: int
) -> None:
    assert Solution().shortestDistance(words, word1, word2) == expected
