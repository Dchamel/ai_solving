"""LeetCode 246. Strobogrammatic Number (Easy)

A strobogrammatic number is a number that looks the same when rotated 180
degrees (upside down). Valid digit mappings: 0->0, 1->1, 6->9, 8->8, 9->6.
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            a, b = num[left], num[right]
            if a not in rotated or rotated[a] != b:
                return False
            left += 1
            right -= 1
        return True
