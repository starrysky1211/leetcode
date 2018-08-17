class Solution1(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # O(m*n)
        m = len(matrix)
        n = len(matrix[0])
        re = []
        # first left-bottom side triangle
        for i in range(m):
            flag = True
            key = matrix[m-1-i][0]
            for j in range(i):
                if j+1 > n-1:
                    break
                flag &= (key == matrix[m-i+j][j+1])
            re.append(flag)
        # then right-top side triangle
        for i in range(n-1):
            flag = True
            key = matrix[0][n-1-i]
            print (0, n-1-i)
            for j in range(i):
                if j+1 > m-1:
                    break
                flag &= (key == matrix[1+j][n-i+j])
            re.append(flag)
        if False in re:
            return False
        else:
            return True
# a simple way that don't get which line is False:
class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        
        return True
