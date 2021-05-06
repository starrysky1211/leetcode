class Solution1(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if not rowIndex:
            return row
        row.append(rowIndex)
        for i in range(1, rowIndex):
            row.append(row[-1]*(rowIndex-i)/(i+1))
        return row
# 35ms Solution1


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if not rowIndex:
            return row
        mid, flag = divmod(rowIndex, 2)
        for i in range(rowIndex):
            row.append(row[-1]*(rowIndex-i)/(i+1))
        return row
# delete an append to be faster
