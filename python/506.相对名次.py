'''
Author: Zander
Description: Edit Here
Date: 2021-08-31 11:18:28
LastEditors: Zander
LastEditTime: 2021-08-31 11:29:06
FilePath: /python/506.相对名次.py
'''
#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashmap = {}
        for i, t in enumerate(score):
            hashmap[t] = i
        sl = sorted(hashmap.keys(), reverse=True)
        for i, k in enumerate(sl):
            if i == 0:
                score[hashmap[k]] = 'Gold Medal'
            elif i == 1:
                score[hashmap[k]] = 'Silver Medal'
            elif i == 2:
                score[hashmap[k]] = 'Bronze Medal'
            else:
                score[hashmap[k]] = str(i+1)
        return score
# @lc code=end

