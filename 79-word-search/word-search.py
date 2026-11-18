class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            # base case: matches every letter
            if i == len(word):
                return True

            # 1. out of bounds
            if (r < 0) or (r == rows) or (c < 0) or (c == cols):
                return False

            # 2. wrong letter (or already used)
            if board[r][c] != word[i]:
                return False

            # marking visited cells
            temp = board[r][c]
            board[r][c] = '#'

            found = (backtrack(r+1, c, i+1) or
                    backtrack(r-1, c, i+1) or
                    backtrack(r, c+1, i+1) or
                    backtrack(r, c-1, i+1))

            # backtrack
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
    
        