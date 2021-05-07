#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rel = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1,
        }
        if len(s) == 1:
            return rel[s]
        head = rel[s[0]]
        res = head
        for c in s[1:]:
            cur = rel[c]
            if head < cur:
                res += cur-2*head
            else:
                res += cur
            head = cur
        return res
# @lc code=end

