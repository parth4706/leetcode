class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        
        x_count_grid = [[1 if grid[i][j] == "X" else 0 for j in range(COLS)] for i in range(ROWS)]

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "X":
                    grid[i][j] = 1
                elif grid[i][j] == "Y":
                    grid[i][j] = -1
                else:
                    grid[i][j] = 0
        
        
        prefix_arr = [[grid[i][j] for j in range(COLS)] for i in range(ROWS)]
        
        
        for i in range(ROWS):
            S_val = 0
            S_x = 0
            for j in range(COLS):
                S_val += grid[i][j]
                S_x += x_count_grid[i][j]
                
                prefix_arr[i][j] = S_val
                x_count_grid[i][j] = S_x
        
        
        c = 0
        
        for j in range(COLS):
            S_val = 0
            S_x = 0
            for i in range(ROWS):
                S_val += prefix_arr[i][j]
                S_x += x_count_grid[i][j]
                
                
                prefix_arr[i][j] = S_val 
                
                
                if S_val == 0 and S_x > 0:
                    c += 1
                    
        return c
