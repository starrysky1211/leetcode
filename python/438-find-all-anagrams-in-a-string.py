class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        l = len(p)
        pC = Counter(p)
        sC = Counter(s[:l-1])
        re = []
        for i in range(len(s)-l+1):
            sC[s[i+l-1]] += 1
            if sC == pC:
                re.append(i)
            sC[s[i]] -= 1
            if sC[s[i]] == 0:
                del(sC[s[i]])
        return re
