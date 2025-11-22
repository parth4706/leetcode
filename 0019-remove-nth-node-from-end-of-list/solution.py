# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        count = 0
        while curr:
            count +=1
            curr = curr.next
        curr = head
        if count != n:
            for i in range(count-n-1):
                curr = curr.next
            curr.next = curr.next.next
            return head
        else:
            return curr.next
