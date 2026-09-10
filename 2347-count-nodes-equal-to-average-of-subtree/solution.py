class Solution(object):
    def averageOfSubtree(self, root):
        res = [0]

        def dfs(root):
            if not root:
                return (0, 0)

            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if total_sum // total_count == root.val:
                res[0] += 1

            return (total_sum, total_count)

        dfs(root)
        return res[0]
