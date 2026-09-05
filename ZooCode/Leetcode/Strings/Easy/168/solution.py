"""LeetCode 168. Excel Sheet Column Title (Easy)

Given an integer columnNumber, return its corresponding column title as it
appears in an Excel sheet (1 -> A, 26 -> Z, 27 -> AA, ...).
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Base-26 with no zero digit: subtract 1 each iteration to map
        # 1..26 -> 0..25 -> 'A'..'Z'.
        result: list[str] = []
        n = columnNumber
        while n > 0:
            n -= 1
            result.append(chr(n % 26 + ord("A")))
            n //= 26
        return "".join(reversed(result))
