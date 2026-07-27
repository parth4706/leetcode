# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        levels = {}
        level_count = {}
        def dfs(root,level):
            level += 1
            if root is None:
                return
            levels[level] = levels.get(level,0)+root.val
            level_count[level] = level_count.get(level,0)+1
            dfs(root.left,level)
            dfs(root.right,level)
            return
        dfs(root,0)
        res = []
        for i in range(1,len(levels)+1):
            res.append(float(levels[i])/float(level_count[i]))
        return res
