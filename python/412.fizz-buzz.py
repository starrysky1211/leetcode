'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 09:33:23
LastEditors: Zander
LastEditTime: 2021-08-19 09:44:04
FilePath: /python/412.fizz-buzz.py
'''
#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(1, n+1)]
        head = 3
        while head <= n:
            res[head-1] = 'Fizz'
            head += 3
        head = 5
        while head <= n:
            res[head-1] = 'Buzz' if res[head-1] != 'Fizz' else 'FizzBuzz'
            head += 5
        return res
# @lc code=end

