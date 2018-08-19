class Solution1(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        re = 0
        for i in S:
            if i in J:
                re += 1
        return re
# a faster solution don't need to traversal J lots of times
class Solution2(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = {}
        for i in S:
            d[i] = d.get(i,0)+1
        print d
        return sum([d[j] for j in J if j in d])
