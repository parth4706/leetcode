class Solution(object):
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 and j == n - 1:
                return grid[i][j], grid[i][j]

            mx = float('-inf')
            mn = float('inf')

            if i + 1 < m:
                a, b = dfs(i + 1, j)
                x = grid[i][j]
                mx = max(mx, x * a, x * b)
                mn = min(mn, x * a, x * b)

            if j + 1 < n:
                a, b = dfs(i, j + 1)
                x = grid[i][j]
                mx = max(mx, x * a, x * b)
                mn = min(mn, x * a, x * b)

            memo[(i, j)] = (mx, mn)
            return mx, mn

        ans = dfs(0, 0)[0]
        return ans % (10**9 + 7) if ans >= 0 else -1
