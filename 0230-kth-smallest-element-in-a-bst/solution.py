# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        c = [0,0]
        def dfs(root):
            if c[0] > k:
                return
            if root is None:
                return
            
            
            dfs(root.left)
            c[0] += 1
            if c[0] == k:
                c[1] = root.val
                return
            dfs(root.right)
            return 
        dfs(root)
        return c[1]
        
