'''
Author: Zander
Description: Edit Here
Date: 2021-08-24 10:44:44
LastEditors: Zander
LastEditTime: 2021-08-24 11:05:30
FilePath: /python/500.键盘行.py
'''
#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if self.judge(w):
                res.append(w)
        return res
        
    def judge(self, word:str) -> bool:
        table = {
            'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
            'Q':1,'W':1,'E':1,'R':1,'T':1,'Y':1,'U':1,'I':1,'O':1,'P':1,
            'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
            'A':2,'S':2,'D':2,'F':2,'G':2,'H':2,'J':2,'K':2,'L':2,
            'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3,
            'Z':3,'X':3,'C':3,'V':3,'B':3,'N':3,'M':3,
        }
        if len(word) <= 1:
            return True
        flag = True
        taker = table[word[0]]
        for c in word[1:]:
            if taker != table[c]:
                flag = False
                break
        return flag
# @lc code=end

