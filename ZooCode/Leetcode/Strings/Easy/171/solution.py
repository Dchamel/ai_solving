"""LeetCode 171. Excel Sheet Column Number (Easy)

Given a string columnTitle that represents the column title as appears in an
Excel sheet, return its corresponding column number (A -> 1, Z -> 26,
AA -> 27, ...).
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord("A") + 1)
        return result
