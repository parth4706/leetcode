class Solution(object):
    def diameterOfBinaryTree(self, root):
        max_d = [0]

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            max_d[0] = max(max_d[0], left + right)

            return max(left, right) + 1

        dfs(root)
        return max_d[0]
