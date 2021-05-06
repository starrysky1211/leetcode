class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s, b = 0, 0
        re = []
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                b += 1
            else:
                if b - s >= 2:
                    re.append([s,b])
                s, b = i, i
        if b - s >= 2:
            re.append([s,b])
        return re
