class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        flag = 0
        sum_ = 0
        for i in d.values():
            if i%2 != 0:
                sum_ += i-1
                flag = 1
            else:
                sum_ += i
        return sum_ + 1 if flag else sum_
