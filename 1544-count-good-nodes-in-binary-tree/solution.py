# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        curr_max = root.val
        c = [0]
        def dfs(root,curr_max):
            if root is None:
                return
            if root.val >= curr_max:
                curr_max = root.val
                c[0]+=1
            
            dfs(root.left,curr_max)
            dfs(root.right,curr_max)
            return c[0]
        return dfs(root,curr_max)
