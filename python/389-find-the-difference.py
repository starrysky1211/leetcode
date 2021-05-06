class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = {}
        for i in s:
            h[i] = h.get(i,0) + 1
        for i in t:
            if i not in h or h[i] == 0:
                return i
            else:
                h[i] -= 1
