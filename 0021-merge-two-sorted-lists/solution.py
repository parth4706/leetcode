# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        lst = []
        curr2 = list2
        while curr:
            lst.append(curr.val)
            curr = curr.next
        while curr2:
            lst.append(curr2.val)
            curr2 = curr2.next 
        lst.sort() 
        h = ListNode(0)
        res = h
        for i in lst:
            res.next = ListNode(i)
            res = res.next
        return h.next
        
