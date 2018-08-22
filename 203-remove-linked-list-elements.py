# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while True:
            if head:
                if head.val == val:
                    head = head.next
                else:
                    break
            else:
                break
        r = head
        while True:
            if not head:
                break
            if not head.next:
                break
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return r
