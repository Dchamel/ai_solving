"""LeetCode 14. Longest Common Prefix (Easy)

Find the longest common prefix string amongst an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        # Vertical scan: compare characters at each index across all strings.
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for other in strs[1:]:
                if i >= len(other) or other[i] != ch:
                    return strs[0][:i]
        return strs[0]
