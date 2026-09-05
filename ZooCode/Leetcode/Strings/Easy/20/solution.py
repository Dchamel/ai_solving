"""LeetCode 20. Valid Parentheses (Easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its opening bracket.
        pairs = {")": "(", "}": "{", "]": "["}
        stack: list[str] = []
        for ch in s:
            if ch in pairs:  # closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(ch)
        return not stack
