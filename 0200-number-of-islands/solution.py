class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set()
        c = 0
        def dfs(i,j):
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1:
                return
            if (i,j) in seen:
                return
            seen.add((i,j))
            if grid[i][j]== "0":
                return
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j]=="1":
                    dfs(i,j)
                    c +=1
        return c
        
