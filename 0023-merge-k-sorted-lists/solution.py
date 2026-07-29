# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        def merge(h1, h2):
            if not h1:
                return h2
            if not h2:
                return h1

            if h1.val > h2.val:
                h1, h2 = h2, h1

            head = h1

            while h1 and h2:
                prev = None

                while h1 and h1.val <= h2.val:
                    prev = h1
                    h1 = h1.next

                prev.next = h2

                h1, h2 = h2, h1

            return head
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                h1 = lists[i]

                if i + 1 < len(lists):
                    h2 = lists[i + 1]
                else:
                    h2 = None

                merged.append(merge(h1, h2))

            lists = merged

        return lists[0]

