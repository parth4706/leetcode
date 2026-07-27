# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        S = 0
        def dfs(root,S):
            if root is None:
                return False
            S += root.val
            if root.left is None and root.right is None:
                if S == targetSum:
                    return True
                else:
                    return False
            return dfs(root.left,S) or dfs(root.right,S)
        return dfs(root,S)

