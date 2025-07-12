class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for rows
        for i in range(9):
            rows = []
            for j in range(9):
                if (board[i][j] not in rows) and board[i][j].isnumeric():
                    rows.append(board[i][j])
                elif (board[i][j] in rows) and board[i][j].isnumeric():
                    return False

        # for columns
        for i in range(9):
            cols = []
            for j in range(9):
                if (board[j][i] not in cols) and board[j][i].isnumeric():
                    cols.append(board[j][i])
                elif (board[j][i] in cols) and board[j][i].isnumeric():
                    return False

        # for 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = []
                for k in range(0, 3):
                    for l in range(0, 3):
                        if (board[i + k][j + l] not in grid) and board[i + k][j + l].isnumeric():
                            grid.append(board[i + k][j + l])
                        elif (board[i + k][j + l] in grid) and board[i + k][j + l].isnumeric():
                            return False
                
        return True