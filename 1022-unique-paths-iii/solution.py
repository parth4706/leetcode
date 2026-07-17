class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        k = [0]
        res= []
        c = 0
        for i in grid:
            for j in i:
                if j == -1:
                    c += 1
        def f(i,j,moves):
            moves += 1
            if i == len(grid) or j == len(grid[0])or i <0 or j<0:
                return
            if grid[i][j] == -1:
                return
            if (i,j) in seen:
                return
            
            if grid[i][j] == 2:
                if moves == len(grid)*len(grid[0])-c:
                    k[0] += 1
                    return
                else:
                    return
            seen.add((i,j))
            f(i+1,j,moves)
            f(i,j+1,moves)
            f(i-1,j,moves)
            f(i,j-1,moves)
            seen.remove((i,j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    f(i,j,0)
                    return k[0]
