"""LeetCode 67. Add Binary (Easy)

Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        bits: list[str] = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord("0")
                i -= 1
            if j >= 0:
                total += ord(b[j]) - ord("0")
                j -= 1
            bits.append(chr(total % 2 + ord("0")))
            carry = total // 2
        return "".join(reversed(bits))
