'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:17:07
LastEditors: Zander
LastEditTime: 2021-08-12 11:30:09
FilePath: /python/225.用队列实现栈.py
'''
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.append(x)
        for i in range(len(self._queue)-1):
            self._queue.append(self._queue.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self._queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

