#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xs = str(x)
        rxs = xs[::-1]
        if rxs == xs:
            return True
        return False
        range = len(xs)

# @lc code=end

