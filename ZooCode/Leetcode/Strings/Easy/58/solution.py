"""LeetCode 58. Length of Last Word (Easy)

Given a string s consisting of words and spaces, return the length of the
last word in the string.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces, then find the last space from the right.
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        end = r
        while r >= 0 and s[r] != " ":
            r -= 1
        return end - r
