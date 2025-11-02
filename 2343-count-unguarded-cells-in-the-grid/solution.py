class Solution:
    def solve(self, grid, r, c, m, n):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for dr, dc in dirs:
            x, y = r + dr, c + dc
            while 0 <= x < m and 0 <= y < n and grid[x][y] not in (-1, 1):
                if grid[x][y] == 0:
                    grid[x][y] = 2
                x += dr
                y += dc

    def countUnguarded(self, m, n, guards, walls):
        grid = [[0]*n for _ in range(m)]
        for r, c in guards: grid[r][c] = 1
        for r, c in walls: grid[r][c] = -1

        for r, c in guards:
            self.solve(grid, r, c, m, n)

        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))
