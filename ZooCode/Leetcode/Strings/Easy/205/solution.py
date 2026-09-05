"""LeetCode 205. Isomorphic Strings (Easy)

Two strings s and t are isomorphic if the characters in s can be replaced to
get t, with a one-to-one mapping between characters.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Two maps: s->t and t->s, ensuring the mapping is bijective.
        map_s: dict[str, str] = {}
        map_t: dict[str, str] = {}
        for a, b in zip(s, t):
            if a in map_s and map_s[a] != b:
                return False
            if b in map_t and map_t[b] != a:
                return False
            map_s[a] = b
            map_t[b] = a
        return True
