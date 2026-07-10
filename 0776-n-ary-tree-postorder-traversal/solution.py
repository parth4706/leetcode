"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def dfs(node):
            if node is None:
                return
            
            for i in node.children:
                dfs(i)
            res.append(node.val)
        dfs(root)
        return res
