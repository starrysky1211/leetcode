# 75.32%
class Solution1(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        if row < 3 or col < 3:
            return 0
        # sum must be 15
        def is_magic(subgrid):
            """
            :type subgrid 3x3 matrix
            :rtype bool
            """
            # distinct and row sum
            al = []
            for r in subgrid:
                if sum(r) != 15:
                    return False
                al += r
            if set(al) != set([1,2,3,4,5,6,7,8,9]):
                return False
            # column sum
            for i in range(3):
                if subgrid[0][i]+subgrid[1][i]+subgrid[2][i]!=15:
                    return False
            # diagonals sum
            if subgrid[0][0]+subgrid[1][1]+subgrid[2][2]!=15:
                return False
            if subgrid[2][0]+subgrid[1][1]+subgrid[0][2]!=15:
                return False
            return True
        # tranversal the grid like conv 3X3
        re = 0
        for r in range(row-2):
            for c in range(col-2):
                subgrid = [grid[r][c:c+3], grid[r+1][c:c+3], grid[r+2][c:c+3]]
                if is_magic(subgrid):
                    re += 1
        return re
