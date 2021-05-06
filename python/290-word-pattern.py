class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        n = len(pattern)
        hashmap = {}
        if n != len(str):
            return False
        for i in range(n):
            head = pattern[i]
            if head in hashmap:
                if hashmap[head] != str[i]:
                    return False
            elif str[i] in hashmap.values():
                return False
            else:
                hashmap[head] = str[i]
        return True
