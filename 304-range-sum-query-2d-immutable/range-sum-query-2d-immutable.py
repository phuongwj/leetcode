class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.prefix = []
        
        for row in matrix:
            prefixRow = []

            for num in row:
                if prefixRow:
                    prefixRow.append(prefixRow[-1] + num)
                else:
                    prefixRow.append(num)
            
            self.prefix.append(prefixRow)
        
        print("HUH: ", self.prefix)
        print("")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for row in range(row1, row2 + 1):
            if col1 == 0:
                total += self.prefix[row][col2]
            else:
                total += self.prefix[row][col2] - self.prefix[row][col1 - 1]

        return total

        """
        rows:
        [1, 2, 0, 1, 5]
        [4, 1, 0, 1, 7]
        [1, 0, 3, 0, 5]

        prefix becomes:
        [1, 3, 3, 4, 9]
        [4, 5, 5, 6, 13]
        [1, 1, 4, 4, 9]
        row1 = 2; col1 = 1; row2 = 4; col2 = 3
        => first loop: 4 - 1 = 3
        """

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)