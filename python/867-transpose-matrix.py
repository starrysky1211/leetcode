class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(A)
        c = len(A[0])
        N = []
        for col in range(c):
            N.append([])
            for row in range(r):
                N[col].append(A[row][col])
        return N
