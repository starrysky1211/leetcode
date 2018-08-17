class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for i in range(n):
            hash1[s[i]] = hash1.get(s[i],0) + 1
            hash2[t[i]] = hash2.get(t[i],0) + 1
        return hash1 == hash2
