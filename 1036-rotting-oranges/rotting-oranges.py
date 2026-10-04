class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        """
        [i-1][j]
        [i+1][j]
        [i][j-1]
        [i][j+1]
        """
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        minute = 0
        grid2 = [ [0]*m for _ in range(n) ]

        for i in range(n):
            for j in range(m):
                grid2[i][j] = grid[i][j]

        # you try all the movements at all spots, and you see that you 
        # cannot change them to 2, then yous hould break
        
        while True:
            
            count = 0
            for i in range(n):
                for j in range(m):

                    if grid[i][j] == 2:

                        for dir in range(len(dx)):
                            newI = i + dx[dir]
                            newJ = j + dy[dir]

                            if newI >= 0 and newJ >= 0 and newI < n and newJ < m:
                                if grid2[newI][newJ] == 1:
                                    count += 1
                                    grid2[newI][newJ] = 2                        

            if count == 0:
                break
            if count >= 1:
                minute += 1
            
            for i in range(n):
                for j in range(m):
                    grid[i][j] = grid2[i][j]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return minute