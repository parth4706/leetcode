# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        h = head
        res = ""
        while h:
            res += str(h.val)
            h = h.next
        if res == res[::-1]:
            return True
        return False

