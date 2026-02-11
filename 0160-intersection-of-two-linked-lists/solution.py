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
        h = headA
        sA = set()
        while h:
            sA.add(h)

            h = h.next
        h = headB
        while h:
            if h in sA:
                return h
            h = h.next

        
