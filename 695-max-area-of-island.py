class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DFS
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        visit = set()
        re = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    stack = [(r,c)]
                    area = 1
                    # start DFS
                    while stack:
                        r,c = stack.pop()
                        # must certify the upper, because the one at right and up side is not in set()
                        # upper
                        if r > 0 and grid[r-1][c] == 1 and (r-1, c) not in visit:
                            stack.append((r-1, c))
                            visit.add((r-1,c))
                            area += 1
                        # lefter
                        if c > 0 and grid[r][c-1] == 1 and (r, c-1) not in visit:
                            stack.append((r, c-1))
                            visit.add((r, c-1))
                            area += 1
                        # downer
                        if r < row-1 and grid[r+1][c] == 1 and (r+1, c) not in visit:
                            stack.append((r+1, c))
                            visit.add((r+1, c))
                            area += 1
                        # righter
                        if c < col-1 and grid[r][c+1] == 1 and (r, c+1) not in visit:
                            stack.append((r, c+1))
                            visit.add((r, c+1))
                            area += 1
                    re = max(re, area)
        return re
