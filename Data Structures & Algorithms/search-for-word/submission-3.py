class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set what rows and cols mean
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i, path):
            # i = # of characters we have matched so far
            if i == len(word):
                return True
        # mark invalid moves
        # [r][c] in path (set), board[r][c] != word[i], OUT OF BOARD BOUNDS
            if (r < 0 or c < 0 or c >= cols or r >= rows):
                return False
            if (r, c) in path: 
                return False
            if board[r][c] != word[i]:
                return False
            path.add((r,c))

            found = (
                dfs(r + 1, c, i + 1, path) or
                dfs(r -1 , c, i + 1, path) or
                dfs(r, c + 1, i + 1, path) or
                dfs(r, c - 1, i + 1, path))

            path.remove((r,c))
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True
        return False

