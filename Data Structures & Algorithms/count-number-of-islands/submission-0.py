class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or c >= cols or r >= rows):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0' # mark as visited. treat as water
            # dfs explore all neighbors, no OR
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
            # CALL dfs again to keep repeating aft 1st before res
                    dfs(r, c)
        return res