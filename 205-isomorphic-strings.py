class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False
        hashmap = {}
        for i in range(n):
            # tranversal two string at the same time, must can be replace
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            elif t[i] in hashmap.values():
                return False
            else:
                hashmap[s[i]] = t[i]
        return True
