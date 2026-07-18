class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = {}
        def dfs(i,j):
            if (i,j) in seen:
                return seen[(i,j)]
            if i == len(grid)-1 and j == len(grid[0])-1:
                seen[(i,j)] = grid[i][j]
                return seen[(i,j)]
            if i == len(grid)-1:
                seen[(i,j)] = dfs(i,j+1) + grid[i][j]
                return seen[(i,j)] 
            if j == len(grid[0])-1:
                seen[(i,j)] = dfs(i+1,j) + grid[i][j]
                return seen[(i,j)] 
            seen[(i,j)] = min(dfs(i+1,j),dfs(i,j+1)) + grid[i][j]
            return seen[(i,j)]
        return dfs(0,0)
