class Solution1(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            row.reverse()
        for r in range(len(A)):
            for c in range(len(A[0])):
                A[r][c] = int(not A[r][c])
        return A
# in order to change 0 to 1 and 1 to 0, we can do int(not a) and also a^1
# so there's a faster solution, but need more space
class Solution2(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[i^1 for i in row[::-1]] for row in A]
