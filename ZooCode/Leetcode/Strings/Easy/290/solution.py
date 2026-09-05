"""LeetCode 290. Word Pattern (Easy)

Given a pattern and a string s, find if s follows the same pattern.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        # Bijective mapping between pattern chars and words.
        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch
        return True
