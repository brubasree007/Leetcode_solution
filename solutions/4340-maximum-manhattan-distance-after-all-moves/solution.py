class Solution:
    def maxDistance(self, moves: str) -> int:
        u = moves.count("U")
        d = moves.count("D")
        l = moves.count("L")
        r = moves.count("R")
        k = moves.count("_")

        return abs(r - l) + abs(u - d) + k
