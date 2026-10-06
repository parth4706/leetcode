class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:

        def dfs(x, y):
            m = len(mat)
            n = len(mat[0])
            if x + 1 < m and mat[x + 1][y] > mat[x][y]:
                return dfs(x + 1, y)
            if x - 1 >= 0 and mat[x - 1][y] > mat[x][y]:
                return dfs(x - 1, y)
            if y + 1 < n and mat[x][y + 1] > mat[x][y]:
                return dfs(x, y + 1)
            if y - 1 >= 0 and mat[x][y - 1] > mat[x][y]:
                return dfs(x, y - 1)

            return [x, y]

        return dfs(0, 0)
