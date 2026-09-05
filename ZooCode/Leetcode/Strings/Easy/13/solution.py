"""LeetCode 13. Roman to Integer (Easy)

Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        prev = 0
        # Walk right-to-left: if a value is smaller than the previous one
        # it is a subtractive pair (IV, IX, XL, ...), so subtract it.
        for ch in reversed(s):
            curr = values[ch]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
