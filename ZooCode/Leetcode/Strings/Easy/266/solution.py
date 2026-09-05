"""LeetCode 266. Palindrome Permutation (Easy)

Given a string s, return true if a permutation of the string could form a
palindrome.
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # A string can be rearranged into a palindrome iff at most one
        # character has an odd frequency.
        odd = 0
        seen: set[str] = set()
        for ch in s:
            if ch in seen:
                seen.remove(ch)
            else:
                seen.add(ch)
        return len(seen) <= 1
