"""LeetCode 344. Reverse String (Easy)

Write a function that reverses a string in-place (the input is given as a
list of characters).
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
