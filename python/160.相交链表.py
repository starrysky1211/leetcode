'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 12:12:04
LastEditors: Zander
LastEditTime: 2021-08-10 12:23:15
FilePath: /python/160.相交链表.py
'''
#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        startA, startB = headA, headB
        lenA, lenB = 0, 0
        while headA:
            lenA += 1
            headA = headA.next
        while headB:
            lenB += 1
            headB = headB.next
        headA, headB = startA, startB
        dl = lenA - lenB
        if dl < 0:
            while dl < 0:
                dl += 1
                headB = headB.next
        else:
            while dl > 0:
                dl -= 1
                headA = headA.next
        # 现在处于同一起跑线
        while headA and headB:
            if headA is headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
# @lc code=end

