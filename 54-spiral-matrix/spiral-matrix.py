class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows, cols = len(matrix), len(matrix[0])
        maxLen = rows * cols

        # bounds
        tRow, bRow, rCol, lCol = 0, rows-1, cols-1, 0

        res = []

        while True:
            
            for i in range(lCol, rCol+1):
                res.append(matrix[tRow][i])
            tRow += 1

            if len(res) >= maxLen: break

            for i in range(tRow, bRow+1):
                res.append(matrix[i][rCol])
            rCol -=1

            if len(res) >= maxLen: break

            for i in reversed(range(lCol, rCol+1)):
                res.append(matrix[bRow][i])
            bRow -= 1

            if len(res) >= maxLen: break

            for i in reversed(range(tRow, bRow+1)):
                res.append(matrix[i][lCol])
            lCol += 1

            if len(res) >= maxLen: break

        return res