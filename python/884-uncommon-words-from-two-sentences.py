class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        return [w for w, c in Counter(A.split()+B.split()).items() if c == 1]
