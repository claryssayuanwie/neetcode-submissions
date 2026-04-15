from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n = num of cols, m = num of rows
        return comb(m + n - 2, m - 1)