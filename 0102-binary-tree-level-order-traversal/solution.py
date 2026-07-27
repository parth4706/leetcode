# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def popleft(self):
        if self.head is None:
            return None

        val = self.head.val

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return val
        
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = Deque()
        seen = set()
        res = []

        q.append(root)
        seen.add(root)
        while q.head is not None:
            
            level = []
            level_size = q.size
            for i in range(level_size): 
                node = q.popleft()
                if node is None:
                    continue
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if level != []:
                res.append(level)
        return res

