'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 11:46:41
LastEditors: Zander
LastEditTime: 2021-08-11 12:00:12
FilePath: /python/202.快乐数.py
'''
#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 探寻规律：4会回到4，2会回到4，3会回到4，5会回到4，6会回到4，7会回到1，8会回到4，9会回到4
        def getSum(num):
            res = 0
            while num > 0:
                num, head = divmod(num, 10)
                res += head**2
            return res
        while n >= 10:
            n = getSum(n)
        if n in [1, 7]:
            return True
        return False
# @lc code=end

