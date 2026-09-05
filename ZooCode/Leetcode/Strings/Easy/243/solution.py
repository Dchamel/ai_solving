"""LeetCode 243. Shortest Word Distance (Easy)

Given an array of strings wordsDict and two strings word1 and word2 that
already exist in the array, return the shortest distance between them.
"""


class Solution:
    def shortestDistance(
        self, wordsDict: list[str], word1: str, word2: str
    ) -> int:
        idx1 = -1
        idx2 = -1
        best = len(wordsDict)
        for i, w in enumerate(wordsDict):
            if w == word1:
                idx1 = i
                if idx2 != -1:
                    best = min(best, idx1 - idx2)
            elif w == word2:
                idx2 = i
                if idx1 != -1:
                    best = min(best, idx2 - idx1)
        return best
