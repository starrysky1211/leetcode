class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res+=4
                    if r>0:
                        res -= grid[r-1][c]
                    if r<row-1:
                        res -= grid[r+1][c]
                    if c>0:
                        res -= grid[r][c-1]
                    if c<col-1:
                        res -= grid[r][c+1]
        return res
                    
                    
