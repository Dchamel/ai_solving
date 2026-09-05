"""LeetCode 293. Flip Game (Easy)

You are playing a Flip Game with a string that contains only + and -.
In one move, flip two consecutive "++" into "--". Return all possible states
after one valid move.
"""


class Solution:
    def generatePossibleNextMoves(self, s: str) -> list[str]:
        result: list[str] = []
        chars = list(s)
        for i in range(len(chars) - 1):
            if chars[i] == "+" and chars[i + 1] == "+":
                chars[i] = "-"
                chars[i + 1] = "-"
                result.append("".join(chars))
                chars[i] = "+"
                chars[i + 1] = "+"
        return result
