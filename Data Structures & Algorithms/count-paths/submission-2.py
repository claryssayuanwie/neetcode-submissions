from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n = num of cols, m = num of rows
        N = m + n - 2
        r = m - 1
        return factorial(N) // (factorial(r) * factorial(N - r))