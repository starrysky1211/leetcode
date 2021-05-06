class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        triangle = [[1]]
        if numRows == 1:
            return triangle
        
        original = [1]
        last = [1]
        for i in range(1,numRows):
            now = original+[last[j]+last[j+1] for j in range(len(last)-1)]+original
            triangle.append(now)
            last = now
        return triangle
            
        
