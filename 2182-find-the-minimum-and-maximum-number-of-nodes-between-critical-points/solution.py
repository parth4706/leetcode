# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        lmin = 1000000
        r = 0
        stk = []
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        prev = head
        curr = head.next
        Next = head.next.next
            


        while curr.next:
            r+= 1
            if ((prev.val < curr.val and Next.val < curr.val) or (prev.val > curr.val and Next.val > curr.val)):
                if stk:
                    lmin = min(lmin,r-stk[-1])
                stk.append(r)
            curr = curr.next
            Next = Next.next
            prev = prev.next
        if len(stk) <2:
            return [-1,-1]
        lmax = stk[-1]-stk[0]
        return [lmin,lmax]

