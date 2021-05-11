#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if l == len(s): return False
        return True
    def isValid2(self, s: str) -> bool:
        pair = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        for c in s:
            if len(stack) == 0:
                if c in pair:
                    return False
                stack.append(c)
            elif c not in pair:
                stack.append(c)
            elif pair[c] != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return len(stack) == 0
# @lc code=end

