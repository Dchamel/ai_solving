"""LeetCode 405. Convert a Number to Hexadecimal (Easy)

Given an integer num, return a string representing its hexadecimal
representation. For negative integers, use two's complement (32-bit).
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        # Mask to 32-bit unsigned to handle negatives via two's complement.
        if num < 0:
            num += 2**32
        digits = "0123456789abcdef"
        result: list[str] = []
        while num > 0:
            result.append(digits[num & 0xF])
            num >>= 4
        return "".join(reversed(result))
