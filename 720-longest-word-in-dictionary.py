class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        s, re = set(['']), ''
        words.sort()
        for w in words:
            if w[:-1] in s:
                s.add(w)
                if len(w) > len(re):
                    re = w
        return re
