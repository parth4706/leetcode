class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        slow.next = None

        
        rev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = rev
            rev = curr
            curr = nxt

        
        l1 = head
        l2 = rev

        while l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2
            l2.next = n1

            l1 = n1
            l2 = n2
