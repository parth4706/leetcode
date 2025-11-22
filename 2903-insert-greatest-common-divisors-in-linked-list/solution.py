# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = ListNode(curr.val)
        sol = res
        while curr and curr.next:
            res.next = ListNode(gcd(curr.val,curr.next.val))
            res.next.next = ListNode(curr.next.val)
            curr = curr.next
            res = res.next.next
        return sol
