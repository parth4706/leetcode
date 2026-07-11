# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
        while head and head.val == val:
            head = head.next
        curr = head    
        while curr:
            while curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head
