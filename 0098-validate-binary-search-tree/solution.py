# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        c = [None]
        def dfs(root):
            
            if root is None:
                return True

            if not dfs(root.left):
                return False
            if c[0] is not None and root.val <= c[0]:
                return False
            
            c[0] = root.val
            
            return dfs(root.right)
        
        return dfs(root)
