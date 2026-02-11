# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h1 = l1
        h2 = l2
        s1 = ""
        s2 = ""
        while h1:
            s1 += str(h1.val)
            h1 = h1.next
        while h2:
            s2 += str(h2.val)
            h2 = h2.next
        s3 = str(int(s1)+int(s2))
        h = ListNode(0)
        curr = h
        for i in s3:
            curr.next = ListNode(int(i))
            curr = curr.next
        return h.next

        
