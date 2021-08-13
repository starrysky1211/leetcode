'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 09:34:36
LastEditors: Zander
LastEditTime: 2021-08-12 10:23:29
FilePath: /python/204.计数质数.py
'''
#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        isprime = [1] * n
        for i in range(2, n):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if prime * i >= n:
                    break
                isprime[prime*i] = 0
        return len(primes)
                

# @lc code=end

