# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        seen = {}
        def dfs(node):
            if node in seen:
                return seen[node]
            if node is None:
                return 0
            seen[node] = 1 + max(dfs(node.left),dfs(node.right))
            return seen[node]
        return dfs(root)
