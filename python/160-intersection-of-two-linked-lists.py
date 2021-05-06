# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la,lb = 0,0
        sa,sb = headA,headB
        while headA:
            la += 1
            headA = headA.next
        while headB:
            lb += 1
            headB = headB.next
        while la > lb:
            sa = sa.next
            la -= 1
        while lb > la:
            sb = sb.next
            lb -= 1
        # now we have two list with the same length
        while sb != sa:
            sb = sb.next
            sa = sa.next
        return sb
