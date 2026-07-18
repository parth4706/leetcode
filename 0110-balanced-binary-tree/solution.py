# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        balanced = [True]


        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            if balanced[0] == False:
                return 0
            right = dfs(node.right)
            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            return 1 + max(dfs(node.left),dfs(node.right))
        dfs(root)
        return balanced[0]
