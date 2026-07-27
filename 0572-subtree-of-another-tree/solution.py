# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return sameTree(l.left,r.left) and sameTree(l.right,r.right)
        def dfs(root):
            if root is None:
                return False
            if sameTree(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)

            

