class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(M), len(M[0])
        N = []
        nc = []
        for i in range(row):
            N.append([])
            for j in range(col):
                N[i].append(0)
        if row == 1 and col == 1:
            return M
        if row == 1:
            for c in range(col):
                if c == 0:
                    N[0][c] = (M[0][c] + M[0][c+1])//2
                elif c == col-1:
                    N[0][c] = (M[0][c] + M[0][c-1])//2
                else:
                    N[0][c] = (M[0][c] + M[0][c-1] + M[0][c+1])//3
            return N
        if col == 1:
            for r in range(row):
                if r == 0:
                    N[r][0] = (M[r][0] + M[r+1][0])//2
                elif r == row-1:
                    N[r][0] = (M[r][0] + M[r-1][0])//2
                else:
                    N[r][0] = (M[r][0] + M[r-1][0] + M[r+1][0])//3
            return N
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    _sum = M[r][c] + M[r+1][c+1] + M[r+1][c] + M[r][c+1]
                    N[r][c] = _sum//4
                elif r == 0 and c == col-1:
                    _sum = M[r][c] + M[r+1][c-1] + M[r+1][c] + M[r][c-1]
                    N[r][c] = _sum//4
                elif r == row-1 and c == 0:
                    _sum = M[r][c] + M[r-1][c+1] + M[r-1][c] + M[r][c+1]
                    N[r][c] = _sum//4
                elif r == row-1 and c == col-1:
                    _sum = M[r][c] + M[r-1][c-1] + M[r-1][c] + M[r][c-1]
                    N[r][c] = _sum//4
                elif r == 0 and c not in (0, col-1):
                    _sum = M[r][c] + M[r][c-1] + M[r][c+1] + M[r+1][c] + M[r+1][c-1] + M[r+1][c+1]
                    N[r][c] = _sum//6
                elif r == row-1 and c not in (0, col-1):
                    _sum = M[r][c] + M[r][c-1] + M[r][c+1] + M[r-1][c] + M[r-1][c-1] + M[r-1][c+1]
                    N[r][c] = _sum//6
                elif c == 0 and r not in (0, row-1):
                    _sum = M[r][c] + M[r][c+1] + M[r-1][c] + M[r-1][c+1] + M[r+1][c] + + M[r+1][c+1]
                    N[r][c] = _sum//6
                elif c == col-1 and r not in (0, row-1):
                    _sum = M[r][c] + M[r][c-1] + + M[r-1][c] + M[r-1][c-1] + M[r+1][c] + M[r+1][c-1]
                    N[r][c] = _sum//6
                elif r not in (0, row-1) and c not in (0, col-1):
                    _sum = M[r][c] + M[r][c-1] + M[r][c+1] + M[r-1][c] + M[r-1][c-1] + M[r-1][c+1] + M[r+1][c] + M[r+1][c-1] + M[r+1][c+1]
                    N[r][c] = _sum//9
        return N
