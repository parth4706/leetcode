# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        c = [float('inf'),None]
        def dfs(root):
            
            if root is None:
                return

            dfs(root.left)
            if c[1] is not None:
                c[0]= min(c[0],abs(c[1]-root.val))
            
            c[1] = root.val
            dfs(root.right)
            return 
        dfs(root)
        return c[0]
