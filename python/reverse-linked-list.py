# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,cur = None,head
        while cur:
            last = cur.next
            cur.next = pre
            if last:
                pre = cur
                cur = last
            else:
                break
        return cur
