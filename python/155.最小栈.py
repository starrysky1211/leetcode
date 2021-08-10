'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 11:47:20
LastEditors: Zander
LastEditTime: 2021-08-10 12:13:17
FilePath: /python/155.最小栈.py
'''
#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    ## TODO 改进方向：因为是栈，用一个二维数组，可以保存下前一个元素进入时的最小状态
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minElement = None
        self.holder = []

    def push(self, val: int) -> None:
        self.minElement = min(self.minElement, val) if not self.minElement is None else val
        self.holder.append(val)

    def pop(self) -> None:
        poped = self.holder.pop()
        if self.minElement == poped and len(self.holder):
            self.minElement = self.holder[0]
            for e in self.holder:
                self.minElement = e if e<self.minElement else self.minElement
        if not len(self.holder):
            self.minElement = None

    def top(self) -> int:
        return self.holder[-1]

    def getMin(self) -> int:
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

